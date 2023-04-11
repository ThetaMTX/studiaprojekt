from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Response


def survey(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        for question in questions:
            response_text = request.POST.get(f'response_{question.id}')
            if response_text:
                survey_response = Response.objects.create(
                    question=question,
                    user=request.user if request.user.is_authenticated else None,
                    response_text=response_text
                )
        return redirect('thank_you')
    return render(request, 'survey.html', {'questions': questions})



def thank_you(request):
    return render(request, 'thank_you.html')

def home(request):
    return render(request, 'home.html')
