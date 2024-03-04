# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Alt text](<WhatsApp Image 2024-03-04 at 13.49.07_e4f502e7.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub


### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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
admin.py
from django.contrib import admin
from .models import Book_db,Book_dbAdmin
admin.site.register(Book_db,Book_dbAdmin)
```

## OUTPUT

![output](<Screenshot 2024-02-28 094235.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully 
