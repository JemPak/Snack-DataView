"""Configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.machine import views as viewMachine
from apps.product import views as viewProduct

urlpatterns = [
    path('product/',                   
        viewProduct.ProductListCreateView.as_view()),  # create and get all products
    path('product/<int:pk>',           
        viewProduct.ProductRetrieveUpdateDestroy.as_view()), # get, update and destroy by id_product
    path('create/machine/',                    
         viewMachine.CreateMachine.as_view()),  # create  machine
    path('machine/',                    
         viewMachine.ListMachine.as_view()),  # list machines
    path('machine/<int:pk>',                    
         viewMachine.MachineDetail.as_view()),  # update and destroy machine
    path('machine/allactive/',
         viewMachine.AllActiveMachines.as_view()),  # get all machines actives        
    path('machine/user/<int:user_id>',
         viewMachine.UserMachines.as_view()),       # get machines filter by user_id
    path('machine/bycity/<str:city>',
         viewMachine.MachinesByCity.as_view()),     # get machines filter by city
]
