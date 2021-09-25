from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=150)
    imgpath = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Branch(models.Model):
    laitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.adress


class Contact(models.Model):
    CONTACTS = [
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL'),
    ]

    type = models.IntegerField(choices=CONTACTS, default=1)
    value = models.CharField(max_length=128)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.value