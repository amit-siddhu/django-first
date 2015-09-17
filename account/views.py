from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Task
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import SignupForm
from .tasks import test

def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/login/")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form 
    })

class TaskIndex(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return the task list order by date published."""
        return Task.objects.order_by('-pub_date')


class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'


def runtask(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	test.delay(task.task_name)
	return HttpResponseRedirect('/account/tasks/')