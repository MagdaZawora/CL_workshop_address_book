from django.db import models
from datetime import datetime
from Address_Book import admin
from django.contrib import admin



class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name

admin.site.register(Person)


class Address(models.Model):
    town = models.CharField(max_length=64)
    street = models.CharField(max_length=64, null=True, blank=True)
    street_number = models.CharField(max_length=128, null=True, blank=True)
    flat_number = models.CharField(max_length=128, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.town, self.street, self.street_number, self.flat_number)

admin.site.register(Address)

class Phone(models.Model):
    phone_number = models.CharField(max_length=64, null=True, blank=True)
    phone_type = models.CharField(max_length=64, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number

admin.site.register(Phone)


class Email(models.Model):
    email = models.CharField(max_length=128, null=True, blank=True)
    email_type = models.CharField(max_length=64, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

admin.site.register(Email)







