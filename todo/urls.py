from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #todo pages
    path('',views.current,name='current'),
    path('createnew/',views.create,name='create'),
    path('<int:todo_pk>/',views.inspecttodo,name='inspecttodo'),
    path('<int:todo_pk>/complete', views.completetodo, name ='completetodo'),
    path('<int:todo_pk>/delete', views.deletetodo, name ='deletetodo'),
    path('completed/',views.displaycompleted, name='displaycompleted'),
]
