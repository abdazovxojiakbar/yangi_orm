from django.urls import path

from page.views import get_person, create_person, detail_person, update_person, delete_person

urlpatterns = [
    path('', get_person, name='person-list'),
    path('create/', create_person, name='person-create'),
    path('detail/<int:pk/', detail_person, name='person-create'),
    path('update/<int:pk/', update_person, name='person-update'),
    path('delete/<int:pk/', delete_person, name='person-delete'),



]