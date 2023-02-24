from django.contrib import admin
from .models import Book, Day, Word, Test, Row

# Register your models here.
admin.site.register(Book)
admin.site.register(Day)
admin.site.register(Word)
admin.site.register(Test)
admin.site.register(Row)