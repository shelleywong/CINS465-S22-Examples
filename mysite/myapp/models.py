from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
