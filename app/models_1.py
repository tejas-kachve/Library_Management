from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length = 1000 , null = True , blank = True)
    price     = models.FloatField(null = True , blank = True)
    author    = models.CharField(max_length= 1000 , null = True , blank=True)
    description  = models.TextField(null = True , blank = True)