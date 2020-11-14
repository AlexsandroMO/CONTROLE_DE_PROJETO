
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index'),
    path('projects/', views.projectlist, name='project-list'),
    path('typeDocuments/', views.documtypelist, name='documment-type-list'),
    path('Subject/', views.Subjectlist, name='Subject-list'),
]
