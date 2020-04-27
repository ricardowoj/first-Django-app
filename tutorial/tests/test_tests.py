from django.test import TestCase

from polls.tests import QuestionModelTests, QuestionIndexViewTests, QuestionDetailViewTests, create_question


class QuestionTestTestCase(TestCase):

    def setUp(self):
        self.case = QuestionModelTests()
        return super().setUp()

    def test_metodo_1(self):
        self.assertTrue(
            hasattr(self.case, 'test_was_published_recently_with_future_question'),
            msg='Crie o teste "test_was_published_recently_with_future_question" no "QuestionModelTests"'
        )
    
    def test_metodo_2(self):
        self.assertTrue(
            hasattr(self.case, 'test_was_published_recently_with_old_question'),
            msg='Crie o teste "test_was_published_recently_with_future_question" no "QuestionModelTests"'
        )

    def test_metodo_3(self):
        self.assertTrue(
            hasattr(self.case, 'test_was_published_recently_with_recent_question'),
            msg='Crie o teste "test_was_published_recently_with_future_question" no "QuestionModelTests"'
        )


class QuestionIndexTestCase(TestCase):

    def setUp(self):
        self.case = QuestionIndexViewTests()
        return super().setUp()

    def test_metodo_1(self):
        self.assertTrue(
            hasattr(self.case, 'test_no_questions'),
            msg='Crie o teste "test_no_questions" no "QuestionIndexViewTests"'
        )
    
    def test_metodo_2(self):
        self.assertTrue(
            hasattr(self.case, 'test_past_question'),
            msg='Crie o teste "test_past_question" no "QuestionIndexViewTests"'
        )

    def test_metodo_3(self):
        self.assertTrue(
            hasattr(self.case, 'test_future_question'),
            msg='Crie o teste "test_future_question" no "QuestionIndexViewTests"'
        )
    
    def test_metodo_4(self):
        self.assertTrue(
            hasattr(self.case, 'test_future_question_and_past_question'),
            msg='Crie o teste "test_future_question_and_past_question" no "QuestionIndexViewTests"'
        )
    
    def test_metodo_5(self):
        self.assertTrue(
            hasattr(self.case, 'test_two_past_questions'),
            msg='Crie o teste "test_two_past_questions" no "QuestionIndexViewTests"'
        )

class QuestionDetailTestCase(TestCase):

    def setUp(self):
        self.case  = QuestionDetailViewTests()
        return super().setUp()

    def test_metodo_1(self):
        self.assertTrue(
            hasattr(self.case, 'test_future_question'),
            msg='Crie o teste "test_future_question" no "QuestionDetailViewTests"'
        )

    def test_metodo_2(self):
        self.assertTrue(
            hasattr(self.case, 'test_past_question'),
            msg='Crie o teste "test_past_question" no "QuestionDetailViewTests"'
        )