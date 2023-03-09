from django.contrib import admin
from .models import Book, Day, Word, Test, Row



class TestAdmin(admin.ModelAdmin):
    search_fields = ['create_user__nickname']


class WordAdmin(admin.ModelAdmin):
    search_fields = ['english', 'korean']


# Register your models here.
admin.site.register(Book)
admin.site.register(Day)
admin.site.register(Word, WordAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Row)
