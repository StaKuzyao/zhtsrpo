from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django import forms
from .models import Question, Streak
import random


class AnswerForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput)
    answer = forms.ChoiceField(widget=forms.RadioSelect)


@login_required
def play(request):
    def has_cyr(text: str) -> bool:
        if not isinstance(text, str):
            return False
        for ch in text:
            low = ch.lower()
            if ('а' <= low <= 'я') or low == 'ё':
                return True
        return False

    def is_russian_question(q: Question) -> bool:
        if not has_cyr(q.text) or not has_cyr(q.correct_answer):
            return False
        options = [q.correct_answer] + list(q.incorrect_answers or [])
        options = [o for o in options if isinstance(o, str) and o.strip()]
        # Все варианты должны содержать кириллицу либо быть числом/знаком
        def ok(opt: str) -> bool:
            return has_cyr(opt) or opt.isdigit()
        return len(options) >= 2 and all(ok(o) for o in options)

    streak, _ = Streak.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Сначала достанем вопрос и выставим варианты, чтобы ChoiceField прошёл валидацию
        qid_raw = request.POST.get('question_id')
        question = get_object_or_404(Question, pk=int(qid_raw)) if qid_raw else None
        form = AnswerForm(request.POST)
        if question:
            opts = [question.correct_answer] + list(question.incorrect_answers or [])
            opts = [o for o in opts if isinstance(o, str) and o.strip()]
            form.fields['answer'].choices = [(o, o) for o in opts]
        if form.is_valid() and question:
            qid = form.cleaned_data['question_id']
            selected = form.cleaned_data['answer']
            correct = question.correct_answer.strip()
            if selected == correct:
                new_streak = streak.increment()
                # Начисляем 1 очко за каждый верный ответ
                request.user.points += 1
                request.user.save(update_fields=['points'])
            else:
                streak.reset()
            return redirect('quiz:play')
    # GET or invalid POST -> serve a new random question
    # Пытаемся выбрать вопрос с минимум 2 вариантами (правильный + 1 неверный)
    question = None
    # Выбираем только русские вопросы
    candidates = list(Question.objects.all())
    random.shuffle(candidates)
    for candidate in candidates[:50]:
        if is_russian_question(candidate):
            question = candidate
            break
    if question:
        options = [question.correct_answer] + list(question.incorrect_answers or [])
        options = [opt for opt in options if isinstance(opt, str) and opt.strip()]
        random.shuffle(options)
        form = AnswerForm(initial={'question_id': question.id})
        form.fields['answer'].choices = [(o, o) for o in options]
    else:
        form = AnswerForm(initial={'question_id': 0})
        form.fields['answer'].choices = []
    return render(
        request,
        'quiz/play.html',
        {
            'question': question,
            'form': form,
            'streak': streak.current_streak,
        },
    )

# Create your views here.
