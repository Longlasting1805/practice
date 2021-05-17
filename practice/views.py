from django.shortcuts import render

# Create your views here.

from practice.models import Question


def index(request):
    questions = Question.objects.all
    context = {
        'questions': questions
    }
    return render(request, "practice/practice.html", context)
