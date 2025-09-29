from django.shortcuts import render, redirect

from .forms import PersonForm
from .models import Person

def get_person(request):
    person = Person.objects.all()
    context = {
        'person': person,
    }
    return render(request, 'person/list.html', context)

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person-list')
    else:
        form = PersonForm()
    return render(request, 'person/create.html', {'form': form})

# nima gap