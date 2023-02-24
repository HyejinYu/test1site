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


class Test(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    comment = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return str(self.create_user.nickname + " : " + str(self.create_date))


class Row(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    answer = models.CharField(null=True, blank=True, max_length=100)
    is_correct = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.test.create_user.nickname + " : " + str(self.test.create_date))
