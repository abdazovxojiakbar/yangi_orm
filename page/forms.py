from django import forms

from page.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
                'fullname',
                'bio',
                'age'
        ]