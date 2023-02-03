from django import forms

from word.models import Book, Day, Word


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'link', 'cover']
        labels = {
            'name': '제목',
            'link': '책 소개 링크',
            'cover': '책 커버',
        }


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['name']
        labels = {
            'name': 'Day명',
        }


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['english', 'korean']
        labels = {
            'english': '영어',
            'korean': '뜻',
        }