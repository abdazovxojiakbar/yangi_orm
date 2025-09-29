from django.urls import path

from page.views import get_person, create_person

urlpatterns = [
    path('', get_person, name='person-list'),
    path('create/', create_person, name='person-create'),
]