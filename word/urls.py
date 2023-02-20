from django.urls import path

from .views import base_views, book_views, day_views, word_views, test_views

app_name = 'word'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('book/create/', book_views.book_create, name='book_create'),
    path('book/modify/<int:book_id>', book_views.book_modify, name='book_modfy'),
    path('book/delete/<int:book_id>', book_views.book_delete, name='book_delete'),
    path('day/<int:day_id>/', day_views.day_detail, name='day_detail'),
    path('day/create/<int:book_id>', day_views.day_create, name='day_create'),
    path('day/modify/<int:day_id>', day_views.day_modify, name='day_modify'),
    path('day/delete/<int:day_id>', day_views.day_delete, name='day_delete'),
    path('word/create/<int:day_id>', word_views.word_create, name='word_create'),
    path('word/delete/<int:word_id>', word_views.word_delete, name='word_delete'),
    path('test/index/<int:book_id>', test_views.test_index, name='test_index'),
    path('test/english_blank/', test_views.english_blank, name='english_blank'),
    path('test/english_blank_check/<int:test_id>', test_views.english_blank_check, name='english_blank_check'),
    path('test/english_blank_practice/', test_views.english_blank_practice, name='english_blank_practice'),
]


