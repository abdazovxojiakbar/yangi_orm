from django import forms
from django.db import models

from page.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
                'fullname',
                'bio',
                'age'
        ]
