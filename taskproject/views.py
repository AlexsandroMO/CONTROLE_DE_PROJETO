from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import TaskForm
#from django.contrib import messages
from .models import MyProject, DocumentStandard

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')

def projectlist(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    cols = ['ID', 'NOME DO PROJETO', 'NOME DA EMPRESA','COMENTÁRIOS', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/projetos.html', {'MyProjects': MyProjects, 'cols':cols})


def documtypelist(request):
    
    DocumentStandards = DocumentStandard.objects.all().order_by('-doc_type') 

    cols = ['ID', 'NOME DO DOCUMENTO', 'TIPO DE DOC','FORMATO', 'NÚMERO DE PAG', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols})
  
  #documment_name', 'doc_type','doc_format','doc_type_page','created_sub','update_sub'