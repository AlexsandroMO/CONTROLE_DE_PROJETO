
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.projectlist, name='project-list'),
    path('typeDocuments', views.documtypelist, name='documment-type-list'),
]
