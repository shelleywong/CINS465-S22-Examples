from django import forms
from . import models
from django.core import validators
from django.core.exceptions import ValidationError

def must_not_be_all_caps(value):
    if value.isupper():
        raise forms.ValidationError("Must not be all caps. Please stop shouting.")
    # always return the cleaned data
    return value

class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label='Your Question',
        max_length=280,
        validators = [
            #validators.validate_slug,
            must_not_be_all_caps,
        ])
    
    def save(self, request):
        q_instance = models.QuestionModel()
        q_instance.question_text = self.cleaned_data["question_text"]
        q_instance.author = request.user
        q_instance.save()
        return q_instance