from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    date_of_release = models.DateField()
    description = models.TextField(null=True)
