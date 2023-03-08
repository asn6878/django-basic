from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request)) #다음과 같이 HttpResponse로 돌려줄 수도있지만 매번 하기 번거로워 django의 shortcut을 이용한다.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("해당 Index의 Question은 존재하지 않습니다!")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're now voting on question %s. hope you made a great choice. I'm serious." % question_id)
