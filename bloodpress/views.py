from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .forms import ResponseForm
from django.contrib import messages


def survey(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data['question']
            question = Question.objects.get(pk=question_id)
            response = form.cleaned_data['response']
            question.responses.create(response_text=response)
            messages.success(request, 'Odpowiedź została zapisana!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Nieprawidłowe dane')
    else:
        form = ResponseForm(questions)
    return render(request, 'survey.html', {'form': form, 'questions': questions})


def thank_you(request):
    return render(request, 'thank_you.html')

def home(request):
    return render(request, 'home.html')
