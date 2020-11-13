from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import TaskForm
#from django.contrib import messages
from .models import MyProject

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')

def projectlist(request):
    MyProjects = MyProject.objects.all().order_by('project_name')
    return render(request, 'taskproject/index.html', {'MyProjects': MyProjects})