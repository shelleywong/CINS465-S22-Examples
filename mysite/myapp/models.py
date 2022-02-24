from django.db import models

import datetime
# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(
        'date published',
        default=datetime.date.today)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question_text + " " + str(self.pub_date) + " " + str(self.likes)
