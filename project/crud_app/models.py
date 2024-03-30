from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publication = models.CharField(max_length=30)
    date_of_publish = models.DateField()
    price = models.IntegerField()
