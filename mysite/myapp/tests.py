from django.test import TestCase
from django.contrib.auth import get_user_model

from . import models

# Create your tests here.
class QuestionTestCase(TestCase):
    def setUp(self):
        user1 = get_user_model().objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
        )
        user1.save()
        user_instance = get_user_model().objects.get(id=1)
        models.QuestionModel.objects.create(
            question_text="lion?",
            author=user_instance
        )

    def test_question_to_str(self):
        """QuestionModel __str__ method correctly prints"""
        lion = models.QuestionModel.objects.get(question_text="lion?")
        self.assertEqual(str(lion), 'lion? john')

class AnswerTestCase(TestCase):
    def setUp(self):
        # create 1st user
        user1 = get_user_model().objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
        )
        user1.save()
        user_instance = get_user_model().objects.get(id=1)
        # create 2nd user
        user2 = get_user_model().objects.create_user(
            'paul',
            'mccartney@thebeatles.com',
            'paulpassword'
        )
        user2.save()
        user_instance2 = get_user_model().objects.get(id=2)
        quest = models.QuestionModel.objects.create(
            question_text="lion?",
            author=user_instance
        )
        models.AnswerModel.objects.create(
            answer_text="yes, lion",
            question = quest,
            author=user_instance2
        )

    def test_answer_to_str(self):
        """AnswerModel __str__ method correctly prints"""
        cat = models.AnswerModel.objects.get(answer_text="yes, lion")
        self.assertEqual(str(cat), 'paul yes, lion')
