from django.test import Client, TransactionTestCase
from django.views import generic
from django.utils import timezone
from django.shortcuts import reverse

from polls.views import IndexView, DetailView, ResultsView, vote
from polls.models import Choice, Question


class ViewsTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        self.qst = Question.objects.create(question_text='Questão 1', pub_date=timezone.now())
        self.choiceA = Choice.objects.create(choice_text='A', question=self.qst)
        self.choiceB = Choice.objects.create(choice_text='B', question=self.qst)
        return super().setUp()

    def test_index_view(self):
        self.assertTrue(
            issubclass(IndexView, generic.ListView),
            msg='A IndexView deve ser um tipo de ListView'
        )
        self.assertEquals(
            IndexView.template_name,
            'polls/index.html',
            msg='O template da IndexView deve ser o arquivo index.html dentro de polls'
        )
        self.assertEquals(
            IndexView.context_object_name,
            'latest_question_list',
            msg='A variável de contexto da lista da IndexView deve ser "latest_question_list"'
        )

    def test_index_responde(self):
        resp = self.client.get('/polls/')
        self.assertEquals(
            resp.status_code,
            200,
            msg='A IndexView deve reponder no caminho "/polls/"'
        )
        resp = self.client.get(reverse('polls:index'))
        self.assertEquals(
            resp.status_code,
            200,
            msg='A IndexView deve reponder noa url nomeada "polls:index"'
        )
    
    def test_detail_view(self):
        self.assertTrue(
            issubclass(DetailView, generic.DetailView),
            msg='A DetailView deve ser um tipo de DetailView'
        )
        self.assertEquals(
            DetailView.template_name,
            'polls/detail.html',
            msg='O template da DetailView deve ser o arquivo detail.html dentro de polls'
        )
        self.assertEquals(
            DetailView.model,
            Question,
            msg='O modelo de resultado da DetailView deve ser "Question"'
        )

    def test_detail_responde(self):
        resp = self.client.get('/polls/{}/'.format(self.qst.pk))
        self.assertEquals(
            resp.status_code,
            200,
            msg='A DetailView deve reponder no caminho "/polls/ID/"'
        )
        resp = self.client.get(reverse('polls:detail', args=[self.qst.id]))
        self.assertEquals(
            resp.status_code,
            200,
            msg='A DetailView deve reponder noa url nomeada "polls:detail"'
        )
    
    def test_results_view(self):
        self.assertTrue(
            issubclass(ResultsView, generic.DetailView),
            msg='A ResultsView deve ser um tipo de DetailView'
        )
        self.assertEquals(
            ResultsView.template_name,
            'polls/results.html',
            msg='O template da ResultsView deve ser o arquivo results.html dentro de polls'
        )
        self.assertEquals(
            ResultsView.model,
            Question,
            msg='O modelo de resultado da ResultsView deve ser "Question"'
        )

    def test_results_responde(self):
        resp = self.client.get('/polls/{}/results/'.format(self.qst.pk))
        self.assertEquals(
            resp.status_code,
            200,
            msg='A ResultsView deve reponder no caminho "/polls/ID/"'
        )
        resp = self.client.get(reverse('polls:results', args=[self.qst.id]))
        self.assertEquals(
            resp.status_code,
            200,
            msg='A ResultsView deve reponder noa url nomeada "polls:results"'
        )

    def test_vote_responde_url(self):
        resp = self.client.post('/polls/{}/vote/'.format(self.qst.pk),{
            'choice': self.choiceA.pk
        })
        self.assertEquals(
            Choice.objects.get(id=self.choiceA.pk).votes,
            1,
            msg='Deve salvar o voto da escolha específica'
        )
        self.assertRedirects(
            resp,
            '/polls/{}/results/'.format(self.qst.id)
        )

    def test_vote_responde_nome(self):
        resp = self.client.post(reverse('polls:vote', args=[self.qst.pk]),{
            'choice': self.choiceA.pk
        })
        self.assertEquals(
            Choice.objects.get(id=self.choiceA.pk).votes,
            1,
            msg='Deve salvar o voto da escolha específica'
        )
        self.assertRedirects(
            resp,
            '/polls/{}/results/'.format(self.qst.id)
        )

    def test_vote_nao_responde(self):
        resp = self.client.post(reverse('polls:vote', args=[self.qst.pk]),{
            'choice': 4
        })
        self.assertEquals(
            resp.context['error_message'],
            'You didn\'t select a choice.'
        )
