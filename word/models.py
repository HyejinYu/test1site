from django.db import models

from common.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(null=True, blank=True, max_length=200)
    cover = models.CharField(null=True, blank=True, max_length=200)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Day(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Word(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    english = models.CharField(max_length=100)
    korean = models.CharField(max_length=200)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.english
