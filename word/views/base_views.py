from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from word.models import Book


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    book_list = Book.objects.order_by('-create_date')
    if kw:
        book_list = book_list.filter(
            Q(name__icontains=kw)
        ).distinct()
    paginator = Paginator(book_list, 10)
    page_obj = paginator.get_page(page)
    context = {'book_list': page_obj, 'page': page, 'kw': kw, 'title_tag': '영어단어 책 리스트'}
    return render(request, 'word/book_list.html', context)

