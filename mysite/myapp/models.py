from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text + " " + str(self.author.username) + " " + str(self.pub_date) + " " + str(self.likes)

class AnswerModel(models.Model):
    answer_text = models.CharField(max_length=280)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)

    def __str__(self):
        return str(self.author.username) + " " + self.answer_text
