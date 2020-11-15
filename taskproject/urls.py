from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('hello/', views.hello),
    path('', views.index, name='index'),
    path('projects/', views.projectlist, name='project-list'),
    path('typeDocuments/', views.documtypelist, name='documment-type-list'),
    path('Subject/', views.Subjectlist, name='subject-list'),
    path('action/', views.Actionlist, name='action-list'),
    path('status/', views.Statuslist, name='status-list'),
    path('employee/', views.Employeelist, name='employee-list'),
]
