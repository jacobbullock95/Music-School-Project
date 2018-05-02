from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        group = Group.objects.get(name='student')
        user.groups.add(group)
        user.save()

        return user
