import json
import os
from django.test import Client, SimpleTestCase
from django.conf import settings
from django.shortcuts import reverse

class AutorTestCase(SimpleTestCase):

    def test_dados_autor(self):
        with open(os.path.join(settings.BASE_DIR, 'autor.json'), 'r') as arquivo:
            autor = json.load(arquivo)
            self.assertNotEquals(
                autor['ra'],
                '',
                msg='Não esqueça de informar seu RA no arquivo "autor.json"'
            )
            self.assertNotEquals(
                autor['nome'],
                '',
                msg='Não esqueça de informar seu nome completo no arquivo "autor.json"'
            )
            self.assertNotEquals(
                autor['email'],
                '',
                msg='Não esqueça de informar seu E-mail @aluno.faculdadeimpacta.com.br no arquivo "autor.json"'
            )



class PollsAppTestCase(SimpleTestCase):

    def setUp(self):
        self.staticFolder = os.path.join(settings.BASE_DIR, 'polls/static')
        return super().setUp()

    def test_app_existe(self):
        self.assertTrue(
            os.path.isdir(os.path.join(settings.BASE_DIR, 'polls')),
            msg='O nome da aplicação deve ser polls (mesma nome da pasta que deve ser criada)!'
        )

    def test_templates_dirs(self):
        self.assertEquals(
            settings.TEMPLATES[0]['DIRS'],
            [os.path.join(settings.BASE_DIR, 'templates')]
        )

    def test_arquivos_estaticos(self):
        self.assertTrue(
            os.path.isdir(self.staticFolder),
            msg='Crie o diretório de arquivos estáticos na aplicação Polls'
        )

    def test_arquivo_css(self):
        caminho = os.path.join(self.staticFolder, 'polls/style.css')
        self.assertTrue(
            os.path.isfile(caminho),
            msg='Crie o arquivo style.css dentro do diretório static/polls'
        )

    def test_carrega_static(self):
        indexPath = os.path.join(settings.BASE_DIR, 'polls/templates/polls/index.html')
        with open(indexPath, 'r') as arquivo:
            dados = arquivo.read()
            self.assertTrue(
                '{% load static %}' in dados,
                msg='Carregue as templates tags STATIC corretamente'
            )
            self.assertTrue(
                '{% static \'polls/style.css\' %}' in dados,
                msg='Utilize a template tag STATIC com o arquivo style.css'
            )
