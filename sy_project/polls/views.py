from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request)) # 다음과 같이 HttpResponse로 돌려줄 수도있지만 매번 하기 번거로워 django의 shortcut을 이용한다.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("해당 Index의 Question은 존재하지 않습니다!") # 얘도 django의 shortcut 기능중 하나다. 이렇게 하면 더 간단하겠지?
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # detail.html로 리디렉션 해주고 에러메시지 template로 전달
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "아무것도 선택하지 않았습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 항상 HttpResponseRedirect 를 해줘야 사용자가 뒤로가기를 눌렀을때 두번 post요청이 되는걸 막는다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

