from django.urls import path
from . import views

app_name = 'salary'

urlpatterns = [
    path('', views.index, name='index'),
    path('excelGood/', views.excelIndex, name='excel'),
    path('salary/', views.salary, name='salary'),

]