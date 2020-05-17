import os
from django.test import SimpleTestCase
from django.contrib import admin
from django.conf import settings

from polls.admin import ChoiceInline, QuestionAdmin
from polls.models import Choice, Question

class ChoiceAdminTestCase(SimpleTestCase):
    
    def test_is_tabular(self):
        self.assertTrue(
            issubclass(ChoiceInline, admin.TabularInline),
            msg="O layout do admin para as escolhas (Choices) deve ser tabelado!"
        )

    def test_model_correto(self):
        self.assertEquals(
            ChoiceInline.model,
            Choice,
            msg="Configure o admin das escolhas (Choice) com o modelo correto de escolhas (Choice)"
        )

    def test_campo_extra(self):
        self.assertEquals(
            ChoiceInline.extra,
            3,
            msg="O admin das escolhas (Choice) deve criar 3 campos de inserção automaticamente"
        )


class QuestionAdminTestCase(SimpleTestCase):
    
    def test_heranca(self):
        self.assertTrue(
            issubclass(QuestionAdmin, admin.ModelAdmin),
            msg="O admin das questões deve ser um ModelAdmin"
        )

    def test_registrado(self):
        self.assertTrue(
            Question in admin.site._registry,
            msg="O admin de questões não foi registrado corretamente"
        )

    def test_tipo_registrado(self):
        qstAdmin = admin.site._registry[Question]
        self.assertEquals(
            type(qstAdmin),
            QuestionAdmin,
            msg="O tipo do admin de questões deveria ser QuestionAdmin"
        )

    def test_inlines_correto(self):
        self.assertTrue(
            ChoiceInline in QuestionAdmin.inlines,
            msg="Configure o QuestionAdmin para inserir escolhas diretamente no seu cadastro!"
        )

    def test_list_display(self):
        resposta = ('question_text', 'pub_date', 'was_published_recently')
        list_display = QuestionAdmin.list_display
        for item in resposta:
            self.assertTrue(
                item in list_display,
                msg='O item "'+item+'" deveria estar na propriedade list_display'
            )

    def test_list_filter(self):
        self.assertTrue(
            'pub_date' in QuestionAdmin.list_filter,
            msg='O item "pub_date" deveria aparecer na propriedade list_filter'
        )

    def test_search_fields(self):
        self.assertTrue(
            'question_text' in QuestionAdmin.search_fields,
            msg='O item "question_text" deveria aparecer na propriedade search_fields'
        )

    def test_fieldsets(self):
        fieldsets = QuestionAdmin.fieldsets
        self.assertTrue(
            len(fieldsets) == 2,
            msg='Devem haver dois fieldsets no Admin de questões!'
        )

    def test_primeiro_fieldset(self):
        fieldset = QuestionAdmin.fieldsets[0]
        configuracao = fieldset[1]

        self.assertDictContainsSubset(
            {'fields': ['question_text']},
            configuracao,
            msg='Fieldset deve ao menos configurar o campo "question_text"'
        )

    def test_segundo_fieldset(self):
        fieldset = QuestionAdmin.fieldsets[1]
        configuracao = fieldset[1]
        self.assertDictContainsSubset(
            {'fields': ['pub_date'], 'classes': ['collapse']},
            configuracao,
            msg='Fieldset deve ao menos configurar o campo "pub_date" e a classe "collapse"'
        )


class AdminPageTestCase(SimpleTestCase):

    def setUp(self):
        self.filePath = os.path.join(settings.BASE_DIR, 'polls/templates/admin/base_site.html')
        return super().setUp()

    def test_pagina_existe(self):
        
        self.assertTrue(
            os.path.isfile(self.filePath),
            msg='Copie o arquivo base_site.html da fonte do Admin do Django (veja no tutorial como fazer!)'
        )

    def test_substitui_header(self):
        with open(self.filePath, 'r') as file:
            dados = file.read()
            self.assertFalse(
                'site_header|default:_(\'Django administration\')' in dados,
                msg='A String contendo "site_header|default:_(\'Django administration\')" deve ser removida!'
            )
            self.assertTrue(
                'Polls Administration' in dados,
                msg='A String contendo "Polls Administration" deve ser inserida!'
            )