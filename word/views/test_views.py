from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
import random

from django.utils import timezone

from word.forms import BookForm
from word.models import Book, Day, Word, Test, TestRow


@login_required(login_url='common:login')
def test_index(request, book_id):
    book_list = Book.objects.order_by('name')
    day_list = Day.objects.order_by('-id')

    context = {"book_id": book_id, "book_list": book_list, "day_list": day_list, "title_tag": '영어단어 시험 선택'}
    return render(request, 'word/test_index.html', context)


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
    test = Test(create_user=request.user, create_date=timezone.now(), score=0)
    test.save()
    word_list = list(word_qset_list)
    random.shuffle(word_list)
    context = {'word_list': word_list[:num_questions], 'day_list': day_list, 'title_tag': "영어 단어 시험보기"}
    return render(request, 'word/english_blank.html', context)


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
    return render(request, 'word/english_blank.html', context)


def english_blank_check(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    if request.method == 'POST':
        word_answer_dict = dict(zip(request.POST.get('words').split(','), request.POST.get('answers').split(',')))
        sorted_word_list = request.POST.get('words').split(',').sort()
        sorted_answer_list = []
        for word in sorted_word_list:
            sorted_answer_list.append(word_answer_dict[word])
        word_qset_list = Word.objects.order_by('id').filter(
            Q(id__in=word_answer_dict.keys())
        ).distinct()
        correct_answer_count = 0
        for word in word_qset_list:
            answer = word_answer_dict[word.id]
            is_correct = (word.english == answer)
            if is_correct:
                correct_answer_count +=1
            test_row = TestRow(test=test, word=word, answer=word_answer_dict[word.id], is_correct=is_correct)
            test_row.save()
        test.score(int(correct_answer_count/len(sorted_word_list)))
        test.save()
        return redirect('word:english_blank_check', test_id=test.id)
    context = {'test': test, 'title_tag': "영어 단어 결과"}
    return render(request, 'word/english_blank_check.html', context)
