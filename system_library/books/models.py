from django.db import models
from common.models import Person

class Author(Person):
    pass

class Category(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    date_of_release = models.DateField()
    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(null=True, blank=True)
