from django.db import models
from django.contrib import admin
class Book_db(models.Model):
    book_name=models.CharField(max_length=20);
    author_name=models.CharField(max_length=20);
    published_year=models.IntegerField(primary_key = "published_year");
    price=models.IntegerField();
    ratings=models.IntegerField();
class Book_dbAdmin(admin.ModelAdmin):
    list_display=("book_name","author_name","published_year","price","ratings")
