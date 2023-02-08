from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from word.forms import BookForm
from word.models import Book


@login_required(login_url='common:login')
def book_create(request):
    if request.method == 'POST':
        print("book_create :  POST")
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.create_date = timezone.now()
            book.create_user = request.user
            book.save()
            return redirect('word:index')
    else:
        print("book_create :  GET")
        form = BookForm()
    context = {'form': form}
    return render(request, 'word/book_form.html', {'form': form})


@login_required(login_url='common:login')
def book_modify(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.create_user and not request.user.is_superuser:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('word:detail', book_id=book.id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('word:detail', question_id=book.id)
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'word/book_form.html', context)


@login_required(login_url='common:login')
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.create_user and not request.user.is_superuser:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('word:detail', book_id=book.id)
    book.delete()
    return redirect('word:index')


@login_required(login_url='common:login')
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book, 'title_tag': (book.name + " Day보기")}
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