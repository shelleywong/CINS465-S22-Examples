from django import forms
from . import models
from django.core import validators
from django.core.exceptions import ValidationError

def must_be_lower(value):
    if value.isupper():
        raise forms.ValidationError("must be all lowercase")
    # always return the cleaned data
    return value

class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label='Your Question',
        max_length=280,
        validators = [
            validators.validate_slug,
            must_be_lower, 
        ])
    
    def save(self):
        q_instance = models.QuestionModel()
        q_instance.question_text = self.cleaned_data["question_text"]
        q_instance.save()
        return q_instance