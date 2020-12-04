from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import CotationForm
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



def docummentypelist(request):
    
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type')
    MyProjects = MyProject.objects.all().order_by('project_name') 
    Subjects = Subject.objects.all().order_by('subject_name') 

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols, 'MyProjects':MyProjects, 'Subjects': Subjects})



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



def Uploadlists(request):
    if request.GET.get('arq'):
        print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'taskproject/upload.html', {'Uploads':Uploads})


def Create_PL(request): #Uso admin /CreatePL

    codes.rotina_carrega_pl()

    return redirect('/')


def Create_LD(request):
    #----------------------------------------------------------
    url = str(request)
    list_get = url.split('&')

    print('\n-----------------------------------------')
    itens = [] 
    for a in range(len(list_get)):
        if list_get[a][:4] == 'acti':
            print('<<-acti->>',list_get[a][7:])
            itens.append(list_get[a][7:])

        elif list_get[a][:4] == 'proj':
            print('<<-proj->>',list_get[a][5:])
            itens.append(list_get[a][5:])

        elif list_get[a][:4] == 'sub=':
            print('<<-sub->>',list_get[a][4:])
            itens.append(list_get[a][4:])

        elif list_get[a][:4] == '_sel':
            print('<<-_sel->>',list_get[a][10:])
            itens.append(list_get[a][10:])

    print('\n-----------------------------------------')

    if len(itens[len(itens)-1]) == 3:
        itens[len(itens)-1] = itens[len(itens)-1][:1]

    elif len(itens[len(itens)-1]) == 4:
        itens[len(itens)-1] = itens[len(itens)-1][:2]

    
    if itens[3] == 'All':
        print('result itens com All=      ', itens[4:])
        list_id = itens[4:]
    else:
        print('result itens sem All=      ', itens[3:])
        list_id = itens[3:]

    result_itens = [itens[:3],list_id]
    print('result = :    ', result_itens[0], '--', result_itens[1])


    if itens[0] == 'create_budget' and len(itens) > 3:
        result = trata_cota.cria_orc(result_itens)

    #---------------------------------------------------------- Sei que tem como fazer isso de forma muito mais simples, mas por hora foi o que consegui fazer. (Estudar como fazer isso com recursos django...)

    DocumentStandards = DocumentStandard.objects.all().order_by('documment_name') 

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    #return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols})
    return redirect('cotation-list')

#---------------------------------------------------------------
def Cotationlist(request):

    Cotations = Cotation.objects.all().order_by('doc_name')
    DocStandards = DocumentStandard.objects.all().order_by('-doc_type')

    new_list = []

    cols = ['NOME DO PROJETO', 'DISCIPLINA', 'NOME DOC.', 'COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. HH','CUSTO DOC.', 'ULTIMA ATUALIZAÇÃO']

    return render(request, 'taskproject/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'new_list':new_list})
	

def EditeCotation(request, id):
    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)

    cols = ['NOME DO PROJETO', 'DISCIPLINA', 'NOME DOC.', 'COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. HH']

    if request.method == 'POST':
        form = CotationForm(request.POST, instance=Cotations)
        if form.is_valid():
            Cotations = form.save()
            return redirect('cotation-list')
        else:
            return render(request, 'taskproject/edite-cotation.html', {'form': form, 'Cotations': Cotations, 'cols':cols}) 

    else:
        return render(request, 'taskproject/edite-cotation.html', {'form': form, 'Cotations': Cotations,'cols':cols})


def DeleteCotation(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Template Deletado com Sucesso!')

    return redirect('/')


#---------------------------------------------------------------

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








""" 
def Create_LD(request):
    #----------------------------------------------------------
    url = str(request)
    list_get = url.split('&')

    if list_get[5][10:] == 'All':
        print('entrou', len(list_get[5][10:]))
        num = 6

    else:
        num = 5

    itens = []  
    itens.append(list_get[1][7:])
    itens.append(list_get[2][5:])
    itens.append(list_get[3][4:])

    for a in range(len(list_get)):
        if a > num:
            itens.append(list_get[a][7:])

    if len(itens[len(itens)-1]) == 3:
        itens[len(itens)-1] = itens[len(itens)-1][:1]

    elif len(itens[len(itens)-1]) == 4:
        itens[len(itens)-1] = itens[len(itens)-1][:2]


    print('\n>>>>>>')
    for a in list_get:
        print(a)

    print('_selected=:      ',list_get[5][13:])


    if itens[0] == 'create_budget' and len(itens) > 3:
        result = trata_cota.cria_orc(itens)


   
  
    
    #---------------------------------------------------------- Sei que tem como fazer isso de forma muito mais simples, mas por hora foi o que consegui fazer. (Estudar como fazer isso com recursos django...)

    DocumentStandards = DocumentStandard.objects.all().order_by('documment_name') 

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA', 'DATA DE CRAÇÃO', 'ULTIMA ATUALIZAÇÃO']

    #return render(request, 'taskproject/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols':cols})
    return redirect('documment-type-list')
    """