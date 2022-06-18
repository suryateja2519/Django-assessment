from django.db import models

# Create your models here.
class Books(models.Model):
    book_title=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    book_pages=models.IntegerField()
    book_price=models.IntegerField()
    book_rating=models.FloatField()