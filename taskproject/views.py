from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import TaskForm
#from django.contrib import messages

from .models import MyProject, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue
import sqlite3
import pandas as pd

import codes
import trata_cota
import delete_itens

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
                doc_type_page = c.doc_type_page
                doc_format = c.doc_format
                print('>>>>>>>>>', doc, doc_type_page, doc_format)
                #new_list.append([doc, doc_type_page, doc_format])
                new_list.append([b.id,b.proj_name,b.subject_name,doc,b.doc_name,doc_type_page,doc_format,b.qt_page,b.qt_doc,b.qt_hh,b.cost_doc,b.update_ct])

    cols = ['NOME DO PROJETO', 'DISCIPLINA', 'NOME DOC.', 'COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. DOC', 'QT. HH','CUSTO DOC.', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'new_list':new_list})
	


def Uploadlists(request):
    if request.GET.get('arq'):
        print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'taskproject/upload.html', {'Uploads':Uploads})


def Create_PL(request):
    # read_all[0] = MyProject
    # read_all[1] = Subject
    # read_all[2] = DocumentStandard
    # read_all[3] = Employee
    # read_all[4] = StatusDoc
    # read_all[5] = Action

    read_all = delete_itens.delete_befor()

    for id in read_all[0]:
        proj = get_object_or_404(MyProject, pk=id)
        proj.delete()

    for id in read_all[1]:
        sub = get_object_or_404(Subject, pk=id)
        sub.delete()

    for id in read_all[2]:
        doc = get_object_or_404(DocumentStandard, pk=id)
        doc.delete()

    for id in read_all[3]:
        emp = get_object_or_404(Employee, pk=id)
        emp.delete()

    for id in read_all[4]:
        st = get_object_or_404(StatusDoc, pk=id)
        st.delete()

    for id in read_all[5]:
        ac = get_object_or_404(Action, pk=id)
        ac.delete()

    codes.ronina_carrega_pl()

    return redirect('/')



def Create_Cotation(request):

    cost = ProjectValue.objects.all()
    cost_proj = []
    for a in cost:
        cost_proj.append([a.cost_by_hh,a.cost_by_doc,a.cost_by_A1])

    if request.GET.get('cota-radio'):
        result = request.GET.get('cota-radio')
        if result == 'option1':
            cost_type = result

        if result == 'option2':
            cost_type = result

        if result == 'option3':
            cost_type = result

        read_cota = delete_itens.delete_cotation()

        for id in read_cota:
            cota = get_object_or_404(Cotation, pk=id)
            cota.delete()

        trata_cota.trata_cotation(cost_type, cost_proj)

    return redirect('/')
    #return render(request, 'taskproject/index.html')

