from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from todos.models.task import Task
from django.urls import reverse
from todos.models.form import ChangeStatusForm, AddForm

from logging import getLogger
logger = getLogger(__name__)


def index(request):
    taskList = Task.objects.all()
    form = ChangeStatusForm()
    context = {'taskList' : taskList, 'form':form}
    return render(request, 'todos/index.html', context)

def detail(request, todoId):
    task = Task.objects.get(id=todoId)
    return render(request, 'todos/detail.html', {'task' : task})

def post(request):
    if request.method == 'GET':
        form = AddForm()
        return render(request, 'todos/post.html', {'form': form})

    if request.method == 'POST':
        name = request.POST.get('name')
        memo = request.POST.get('memo')
        task = Task()
        task.create()
        task.setName(name)
        task.setMemo(memo)
        return HttpResponseRedirect(reverse('todos:index'))

def changeStatus(request, *args, **kwargs):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('todos:index'))
    status = request.POST.get('status')
    todoId = request.POST.get('todoId')
    task = get_object_or_404(Task, pk=todoId)
    task.setStatus(status)
    if task.isDone():
        task.Done()
    return HttpResponseRedirect(reverse('todos:index'))

def delete(request, todoId):
    task = get_object_or_404(Task, pk=todoId)
    task.delete()
    return HttpResponseRedirect(reverse('todos:index'))
