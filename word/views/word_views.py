from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.utils import timezone

from word.forms import BookForm, WordForm
from word.models import Day, Word


@login_required(login_url='common:login')
def word_create(request, day_id):
    form = WordForm(request.POST)
    day = get_object_or_404(Day, pk=day_id)
    if request.user != day.create_user and not request.user.is_superuser:
        messages.error(request, '등록권한이 없습니다.')
        return redirect('word:day_detail', day_id=day.id)
    if form.is_valid():
        word = form.save(commit=False)
        word.create_date = timezone.now()
        word.create_user = request.user
        word.day = day
        word.save()
        return redirect('{}#english'.format(resolve_url('word:day_detail', day_id=word.day.id)))
    return render(request, 'word/day_detail.html', {'form': form})


@login_required(login_url='common:login')
def word_delete(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.user != word.create_user and not request.user.is_superuser:
        messages.error(request, '등록권한이 없습니다.')
        return redirect('word:day_detail', day_id=word.day.id)
    day_id = word.day.id
    word.delete()
    return redirect('word:day_detail', day_id)
