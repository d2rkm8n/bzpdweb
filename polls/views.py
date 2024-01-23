from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Question


@login_required
def polls(request):
    list_questions = [question for question in Question.objects.all()
                      if request.user.userprofile.department == question.department]

    result = {'list_questions': list_questions}
    return render(request, 'polls/polls.html', result)
