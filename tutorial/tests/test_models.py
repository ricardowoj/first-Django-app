import datetime
from django.utils import timezone
from django.test import TransactionTestCase
from django.contrib import admin
from polls.models import Choice, Question


class QuestionTestCase(TransactionTestCase):

    def setUp(self):
        Question.objects.create(question_text="Questão 1", pub_date=timezone.now())
        return super().setUp()

    def test_adiciona_questao(self):
        questao1 = Question.objects.create(question_text="Questão Nova", pub_date=timezone.now())
        questao2 = Question.objects.all()[1]
        self.assertEquals(questao1.question_text, questao2.question_text)
        self.assertEquals(questao1.pub_date, questao2.pub_date)

    def test_atributos_admin(self):
        questao = Question.objects.all()[0]
        self.assertEquals(
            questao.was_published_recently.admin_order_field,
            'pub_date',
            msg='Configure o campo "was_published_recently" para o admin ser ordenável péla "pub_date"'
        )
        self.assertTrue(
            questao.was_published_recently.boolean,
            msg='O tipo do campo "was_published_recently" deve ser "boolean" para o admin'
        )
        self.assertEquals(
            questao.was_published_recently.short_description,
            'Published recently?',
            msg='Configure o campo "was_published_recently" para o admin com a descrição correta'
        )


    def test_texto_representativo(self):
        questao = Question.objects.all()[0]
        self.assertEquals(
            questao.__str__(),
            'Questão 1',
            msg='Crie o método __str__ no objeto Question mostrando o seu texto.'
        )

    def test_publicado_recentemente(self):
        ontem = timezone.now() - datetime.timedelta(hours=23)
        anteOntem = timezone.now() - datetime.timedelta(hours=36)
        questao1 = Question.objects.get(question_text='Questão 1')
        questao2 = Question.objects.create(question_text='Questão 2', pub_date=ontem)
        questao3 = Question.objects.create(question_text='Questão 3', pub_date=anteOntem)
        self.assertTrue(questao1.was_published_recently())
        self.assertTrue(questao2.was_published_recently())
        self.assertFalse(questao3.was_published_recently())

    def test_site_admin(self):
        self.assertTrue(Question in admin.site._registry)


class ChoiceTestCase(TransactionTestCase):

    def setUp(self):
        self.questao = Question.objects.create(question_text='Questão 1', pub_date=timezone.now())
        Choice.objects.create(choice_text='Alternativa A', question=self.questao)
        return super().setUp()

    def test_adiciona_escolha(self):
        escolhaB = Choice.objects.create(choice_text='Alternativa B', question=self.questao)
        escolha = Choice.objects.all()[1]
        self.assertEquals(escolha.choice_text, escolhaB.choice_text)
        self.assertEquals(escolha.votes, 0)
        self.assertEquals(escolha.question, self.questao)

    def test_texto_representativo(self):
        escolha = Choice.objects.all()[0]
        self.assertEquals(
            escolha.__str__(),
            'Alternativa A',
            msg='Crie o método __str__ no objeto Choice mostrando o seu texto.'
        )