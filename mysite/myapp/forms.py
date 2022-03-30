from django import forms
from django.core import validators
#from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

from . import models

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
    image = forms.ImageField(
        label="Image File",
        required = False
    )
    image_description = forms.CharField(
        label='Image Description',
        max_length=280,
        required=False
    )

    def save(self, request):
        q_instance = models.QuestionModel()
        q_instance.question_text = self.cleaned_data["question_text"]
        q_instance.image = self.cleaned_data["image"]
        q_instance.image_description = self.cleaned_data["image_description"]
        q_instance.author = request.user
        q_instance.save()
        return q_instance

class AnswerForm(forms.Form):
    answer_text = forms.CharField(
        label='Your Answer',
        max_length=280,
        validators = [
            must_not_be_all_caps,
            validators.MinLengthValidator(2, "Must be at least 2 characters.")
        ])

    def save(self, request, quest_id):
        q_instance = models.QuestionModel.objects.get(id=quest_id)
        a_instance = models.AnswerModel()
        a_instance.answer_text = self.cleaned_data["answer_text"]
        a_instance.author = request.user
        a_instance.question = q_instance
        a_instance.save()
        return a_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
