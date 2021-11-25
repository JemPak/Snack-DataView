from apps.machine.models import Machine
from apps.machine.serializers import MachineSerializer
from rest_framework import generics

from django.shortcuts import get_list_or_404


class CreateMachine(generics.CreateAPIView):
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()


class ListMachine(generics.ListAPIView):
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()

class MachineDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  MachineSerializer
    queryset = Machine.objects.all()

class UserMachines(generics.ListAPIView): # filter by user_id
    serializer_class = MachineSerializer
    
    def get_queryset(self):
        queryset = get_list_or_404(Machine, user_id=self.kwargs["user_id"])
        return queryset

class MachinesByCity(generics.ListAPIView): # filter by city
    serializer_class= MachineSerializer
    
    def get_queryset(self):
        queryset = get_list_or_404(Machine, city=self.kwargs["city"])
        return queryset

class AllActiveMachines(generics.ListAPIView): # all active machines
    serializer_class= MachineSerializer
    
    def get_queryset(self):
        queryset = Machine.objects.filter(is_activate=True)
        return queryset

