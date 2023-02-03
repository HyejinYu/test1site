from django.contrib import admin
from .models import Book, Day, Word

# Register your models here.
admin.site.register(Book)
admin.site.register(Day)
admin.site.register(Word)