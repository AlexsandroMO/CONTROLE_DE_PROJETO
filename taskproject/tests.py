from django.test import TestCase

# Create your tests here.

#admin-admin {% url 'admin-admin' %}

#https://www.treinaweb.com.br/blog/templates-gratuitos-para-aplicacoes-administrativas/
#Apliocações WEB



#inner join DJANGO
#https://stackoverflow.com/questions/48128714/how-to-make-an-inner-join-in-django

#https://pt.stackoverflow.com/questions/458410/consulta-de-tabela-associativa-no-django


#Django CRUD
#https://pythonacademy.com.br/blog/desenvolvimento-web-com-python-e-django-view


#para carregar planilhas digitar http://127.0.0.1:8000/CreatePL no navegador direto e zerar o db

#FILTROS
#https://www.alura.com.br/artigos/django-query-sets-e-orm?gclid=CjwKCAiA_Kz-BRAJEiwAhJNY790u5nNqo3kxpZnNDMk2BNk8nWXaR_oRCb9QJIiFQM4ePufwlupkPRoCRI4QAvD_BwE

""" class ProjectValue(models.Model): #Upload de arquivos
    cost_hh = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cost_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cost_A1 = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.cost_hh) """


#03001001213 - itau


#pip install django-crispy-forms
#{% load crispy_forms_tags %}





'''
from datetime import datetime
data_inicial = request.GET.get('data_inicial')
data_final = request.GET.get('data_final')
# supondo que a data esteja no formato "%Y-%m-%d
dI = datetime.strptime(data_inicial, "%Y-%m-%d")
dF = datetime.strptime(data_final, "%Y-%m-%d")

objs = Job.objects.filter(data_initial__gte=dI,data_final__lte=dF)'''


#https://bootstrapious.com/tutorial/files/sidebar.zip       <<<  Donload de modelo de templte page
#https://bootstrapious.com/p/bootstrap-sidebar




# {% load static %}
# {% block content %}{% endblock %}


#https://pt.stackoverflow.com/questions/421135/como-fazer-redirect-na-p%C3%A1gina-com-django