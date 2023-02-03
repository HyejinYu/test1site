from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
import random

from word.forms import BookForm
from word.models import Book, Day, Word


@login_required(login_url='common:login')
def test_index(request, book_id):
    book_list = Book.objects.order_by('name')
    day_list = Day.objects.order_by('name')
    context = {"book_id": book_id, "book_list": book_list, "day_list": day_list}
    return render(request, 'word/test_index.html', context)


@login_required(login_url='common:login')
def english_blank(request):
    str_days = request.POST.get('days')
    num_questions = int(request.POST.get('num_questions'))
    days = str_days.split(',')
    print("num_questions : ", num_questions)
    word_qset_list = Word.objects.order_by('-day')
    word_qset_list = word_qset_list.filter(
        Q(day__pk__in=days)
    ).distinct()
    word_list = list(word_qset_list)
    random.shuffle(word_list)
    context = {'word_list': word_list[:num_questions]}
    return render(request, 'word/english_blank.html', context)


@login_required(login_url='common:login')
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'word/book_detail.html', context)


    '''
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')


@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)
'''