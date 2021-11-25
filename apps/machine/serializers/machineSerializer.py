from rest_framework import serializers
from apps.machine.models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
    
    def to_representation(self, obj):
        machine = Machine.objects.get(id_machine=obj.id_machine)
        return {
            "id_machine"        : machine.id_machine,
            "user_id"           : machine.user_id,
            "city"              : machine.city,
            "address"           : machine.address,
            "type_machine"      : machine.type_machine,
            "date_create"       : machine.date_create,
            "is_activate"       : machine.is_activate,
            "balance_machine"   : machine.balance_machine,
        }