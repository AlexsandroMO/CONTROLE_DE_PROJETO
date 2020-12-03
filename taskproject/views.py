from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import TaskForm
#from django.contrib import messages
from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue


from decimal import Decimal
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

    MyProjects = MyProject.objects.all().order_by('-project_name')
    cols = ['NOME DO PROJETO', 'NOME DA EMPRESA','COMENTÁRIOS', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/projetos.html', {'MyProjects': MyProjects, 'cols':cols})



def Pagetypelist(request):
    
    pagets = PageT.objects.all()

    return render(request, 'taskproject/pages-type.html', {'pagets': pagets})



def Doctypelist(request):
    
    docts = DocT.objects.all()

    return render(request, 'taskproject/doc-type.html', {'docts': docts})



def documtypelist(request):
    
    DocumentStandards = DocumentStandard.objects.all().order_by('documment_name') 

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

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

    codes.rotina_carrega_pl()

    return redirect('/')


def Create_LD(request):
    #----------------------------------------------------------
    url = str(request)
    list_get = url.split('&')

    itens = []
    itens.append(list_get[1][7:])

    for a in range(len(list_get)):
        #print('----', list_get[a][7:], a)
        if a > 3:
            #print('>>>>>>>', list_get[a][7:], len(list_get[a][7:]))
            itens.append(list_get[a][7:])

    if len(itens[len(itens)-1]) == 3:
        itens[len(itens)-1] = itens[len(itens)-1][:1]

    elif len(itens[len(itens)-1]) == 4:
        itens[len(itens)-1] = itens[len(itens)-1][:2]

    print('\n\n-----------------------------------', itens, len(itens))
    #print('\n\n-----------------------------------', request.GET)

    if itens[0] == 'create_LD' and len(itens) > 1:
        result = trata_cota.cria_orc(itens)
        print(result)

    #---------------------------------------------------------- Sei que tem como fazer isso de forma muito mais simples, mas por hora foi o que consegui fazer. (Estudar como fazer isso com recursos django...)



    DocumentStandards = DocumentStandard.objects.all().order_by('documment_name') 

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols})
    #return redirect('/')





def Create_Cotation(request):

    cost = ProjectValue.objects.all()

    cost_proj = []
    if cost:
        #print('Entrou!!!!!!!!!!!!!!!!!!')
        for a in cost:
            cost_proj.append([Decimal(a.cost_by_hh),Decimal(a.cost_by_doc),Decimal(a.cost_by_A1)])

        cost_proj = cost_proj[0]

    if request.GET.get('cota-radio'):
        cost_type = request.GET.get('cota-radio')

        read_cota = delete_itens.delete_cotation()

        for id in read_cota:
            cota = get_object_or_404(Cotation, pk=id)
            cota.delete()

        trata_cota.trata_cotation(cost_type, cost_proj)

    return redirect('/')
    #return render(request, 'taskproject/index.html')

























   # for a in request.GET['action']:
    #     print('>>>>>', a)

    # print('\n-----------------------------------')

    



    # if '_selected_action' in request.POST: #verifica se _selected_action foi enviado na requisição
    #     variavel = request.POST['_selected_action']
    #     print('-----------SELECTED:::: ', variavel)

    # if request.GET.get('_selected_action'):
    #     print('----------------------entrou', request.GET.get('_selected_action')[0])


    # for a in request.GET.get('_selected_action'):
    #     print(a)

    #if request.GET.get('action'):
        #print('----------------------entrou action :', request.GET.get('action'))
