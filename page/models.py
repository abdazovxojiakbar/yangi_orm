from django.db import models

# Create your models here.

class Person (models.Model):
    fullname = models.CharField(max_length=200)
    bio = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "person"

