from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from word.forms import BookForm, DayForm
from word.models import Book, Day


@login_required(login_url='common:login')
def day_create(request, book_id):
    print("day_create")
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        print("day_create :  POST")
        form = DayForm(request.POST)
        if form.is_valid():
            print("day_create :  POST is valid")
            day = form.save(commit=False)
            day.create_date = timezone.now()
            day.create_user = request.user
            day.book = book
            day.save()
            return redirect('word:book_detail', book_id=book.id)
    else:
        print("day_create :  GET")
        form = DayForm()
    return render(request, 'word/day_form.html', {'form': form, 'title_tag': (book.name + 'Day 등록')})


def day_modify(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    if request.user != day.create_user and not request.user.is_superuser:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('word:book_detail', book_id=day.book.id)
    if request.method == 'POST':
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            day = form.save()
            return redirect('word:book_detail', book_id=day.book.id)
    else:
        form = DayForm(instance=day)
    context = {'form': form, 'title_tag': (day.book.name + ' > ' + day.name + ' 수정')}
    return render(request, 'word/day_form.html', context)


def day_delete(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    if request.user != day.create_user and not request.user.is_superuser:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('word:book_detail', book_id=day.book.id)
    else:
        day = get_object_or_404(Day, pk=day_id)
        if request.user != day.create_user and not request.user.is_superuser:
            messages.error(request, '수정권한이 없습니다.')
            return redirect('word:book_detail', book_id=day.book.id)
        book_id = day.book.id
        print("book_id :", book_id)
        day.delete()
    return redirect('word:book_detail', 1)


def day_detail(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    context = {'day': day, 'title_tag': (day.book.name + " > " + day.name)}
    return render(request, 'word/day_detail.html', context)
