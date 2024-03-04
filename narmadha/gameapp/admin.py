from django.contrib import admin

# Register your models here.
from .models import Book_db,Book_dbAdmin
admin.site.register(Book_db,Book_dbAdmin)