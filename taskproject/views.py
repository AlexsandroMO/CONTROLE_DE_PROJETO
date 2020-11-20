from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import TaskForm
#from django.contrib import messages
from .models import MyProject, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload
import sqlite3
import pandas as pd

import codes

def hello(request):

    return HttpResponse('<h1>Hello!</h1>')


def index(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')

    return render(request, 'taskproject/index.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations})


def projectlist(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    cols = ['NOME DO PROJETO', 'NOME DA EMPRESA','COMENTÁRIOS', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/projetos.html', {'MyProjects': MyProjects, 'cols':cols})



def documtypelist(request):
    
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 

    cols = ['NOME DO DOCUMENTO', 'TIPO DE DOC','FORMATO', 'NÚMERO DE PAG', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols})



def Subjectlist(request):
    
    Subjects = Subject.objects.all().order_by('-subject_name') 

    return render(request, 'taskproject/disciplinas.html', {'Subjects': Subjects})



def Actionlist(request):
    
    Actions = Action.objects.all().order_by('-action_type') 

    return render(request, 'taskproject/action.html', {'Actions': Actions})



def Statuslist(request):
    
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status') 

    return render(request, 'taskproject/status-doc.html', {'StatusDocs': StatusDocs})



def Employeelist(request):
    
    Employees = Employee.objects.all().order_by('-emp_name')
    cols = ['NOME DO COLABORADOR', 'CARGO', 'REGISTRO', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/employee.html', {'Employees': Employees, 'cols':cols})


def Cotationlist(request):

    Cotations = Cotation.objects.all().order_by('-proj_name')
    DocStandards = DocumentStandard.objects.all().order_by('doc_type')

    new_list = []
    for b in Cotations:
        for c in DocStandards:
            if b.doc_name_id == c.id:
                doc = c.documment_name

        new_list.append([b.id,b.proj_name,b.subject_name,doc,b.doc_name,b.qt_page,b.qt_doc,b.qt_hh,b.cost_hh,b.cost_doc,b.update_ct])

    cols = ['NOME DO PROJETO', 'DISCIPLINA', 'NOME DOC.', 'COD. DOC.', 'QD. FOLHAS', 'QT. DOC', 'QT. HH', 'CUSTO HH','CUSTO DOC.', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'new_list':new_list})
	


def Uploadlists(request):
    if request.GET.get('arq'):
        print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'taskproject/upload.html', {'Uploads':Uploads})


def Create_PL(request):
    codes.ronina_carrega_pl()

    return redirect('/')