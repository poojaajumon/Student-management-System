from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('insert',views.insert),
    path('delete/<id>',views.delete),
    path('edit/<id>',views.edit),
    path('update/<id>',views.update),
]