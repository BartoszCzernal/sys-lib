from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)

    class Meta:
        abstract = True

class PersonContant(Person):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    #https://en.wikipedia.org/wiki/Telephone_numbering_plan

    class Meta:
        abstract = True