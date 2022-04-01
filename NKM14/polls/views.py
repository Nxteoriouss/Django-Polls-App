from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'olls/index.html', context)
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))





def detail(request, question_id):
    # try:
    #     question = Question.object.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls/detail.html', {'question':question})
    
    #A shortcut: get_object-or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    

# def index(request):
#     return HttpResponse("Hello, Welcome to my website")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of the question %s."
#     return HttpResponse(response % question_id)

# def vote(request,question_id):
#     return HttpResponse("You,re voting on question %s" % question_id)
