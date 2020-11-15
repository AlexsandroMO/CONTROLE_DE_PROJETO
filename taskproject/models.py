from django.db import models


class MyProject(models.Model): #Títulos de projeto

    project_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    comments = models.TextField()
    created_proj = models.DateTimeField(auto_now_add=True)
    update_proj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Subject(models.Model): #Disciplinas do Projeto

    subject_name = models.CharField(max_length=255)
    created_sub = models.DateTimeField(auto_now_add=True)
    update_sub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class DocumentStandard(models.Model): #Documentos de Projeto

    documment_name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=3)
    doc_format = models.CharField(max_length=15)
    doc_type_page = models.CharField(max_length=2)
    created_doc = models.DateTimeField(auto_now_add=True)
    update_doc = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.doc_type


class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255)
    emp_office = models.CharField(max_length=255)
    emp_contrato = models.CharField(max_length=20)
    created_emp = models.DateTimeField(auto_now_add=True)
    update_emp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name


class StatusDoc(models.Model): #Lista de Status do Projeto

    doc_status = models.CharField(max_length=50)
    created_st = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.doc_status


class Action(models.Model): #Lista de Acões

    action_type = models.CharField(max_length=12)
    created_st = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.action_type