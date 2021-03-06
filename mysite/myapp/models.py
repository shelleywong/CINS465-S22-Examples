
#import datetime
from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/',
        null = True
    )
    image_description = models.CharField(
        max_length=280,
        null = True
    )

    def __str__(self):
        return self.question_text + " " + str(self.author.username)

class AnswerModel(models.Model):
    answer_text = models.CharField(max_length=280)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)

    def __str__(self):
        return str(self.author.username) + " " + self.answer_text
