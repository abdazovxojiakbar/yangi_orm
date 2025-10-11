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

def detail_person(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {
        'person': person,

    }
    return render(request, 'person/detail.html', context)

def update_person(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person-list')
    else:
        form = PersonForm(instance=person)
        return render(request, 'person/create.html', {'form': form})

def delete_person(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person-list')
    else:
        return render(request, 'person/delete.html', {'person': person})


