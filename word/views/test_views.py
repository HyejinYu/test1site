from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
import random, math

from django.utils import timezone

from word.forms import BookForm
from word.models import Book, Day, Word, Test, Row


@login_required(login_url='common:login')
def test_index(request, book_id):
    book_list = Book.objects.order_by('name')
    day_list = Day.objects.order_by('-id')

    context = {"book_id": book_id, "book_list": book_list, "day_list": day_list, "title_tag": '영어단어 시험 선택'}
    return render(request, 'word/test_index.html', context)


#시험 화면
@login_required(login_url='common:login')
def english_blank(request):
    str_days = request.POST.get('days')
    num_questions = int(request.POST.get('num_questions'))
    days = str_days.split(',')
    day_list = Day.objects.order_by('name').filter(
        Q(id__in=days)
    ).distinct()
    word_qset_list = Word.objects.order_by('-day')
    word_qset_list = word_qset_list.filter(
        Q(day__pk__in=days)
    ).distinct()
    test = Test(create_user=request.user, create_date=timezone.now(), score=0, comment="")
    for day in day_list:
        test.comment = test.comment + "[" + day.book.name + "]" + day.name + ", "
    test.comment = test.comment[:-2]
    test.save()
    word_list = list(word_qset_list)
    random.shuffle(word_list)
    test_list = word_list[:num_questions]

    for word in test_list:
        row = Row.objects.create(test=test, word=word, is_correct=False)
        row.save()

    context = {'word_list': test_list, 'day_list': day_list, 'test': test, 'title_tag': "영어 단어 시험보기"}
    return render(request, 'word/english_blank.html', context)


# 영어 시험 연습
@login_required(login_url='common:login')
def english_blank_practice(request):
    str_days = request.POST.get('days')
    num_questions = int(request.POST.get('num_questions'))
    days = str_days.split(',')
    day_list = Day.objects.order_by('name').filter(
        Q(id__in=days)
    ).distinct()
    word_qset_list = Word.objects.order_by('-day')
    word_qset_list = word_qset_list.filter(
        Q(day__pk__in=days)
    ).distinct()
    word_list = list(word_qset_list)
    random.shuffle(word_list)
    context = {'word_list': word_list[:num_questions], 'day_list': day_list, 'title_tag': "영어 단어 시험 연습"}
    return render(request, 'word/english_blank_practice.html', context)


#시험 결과처리 및 시험 결과 보기
def english_blank_check(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    test.end_date = timezone.now()
    if request.method == 'POST':
        question_answer_dict = dict(zip(request.POST.getlist('question'), request.POST.getlist('answer')))
        correct_answer_count = 0
        for row in test.row_set.all():
            row.answer = question_answer_dict[str(row.id)]
            if row.word.english == row.answer:
                correct_answer_count +=1
                row.is_correct = True
            row.save()
        test.score = round(correct_answer_count/test.row_set.all().count()*100)
        test.save()
        return redirect('word:english_blank_check', test_id=test.id)

    context = {'test': test, 'title_tag': "영어 단어 시험 결과"}
    return render(request, 'word/english_blank_check.html', context)


#나의 시험 결과
def my_test_result(request):
    mytest = Test.objects.filter(create_user=request.user).order_by('-id')
    context = {'mytest': mytest, 'title_tag': "시험 결과 리스트"}
    return render(request, 'word/my_test_list.html', context)