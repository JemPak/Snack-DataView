from django.db import models

class Machine(models.Model):
    machines=(
        (0,'Granos'),
        (1,'Granos chicos'),
        (2,'Mayor capacidad'),
        (3, 'Maquina estandar'),
    )

    id_machine = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField("user_id", null=True)
    city = models.CharField("City", max_length=50, null=True, blank=False)
    address=models.CharField("Address", max_length=200, null=True, blank=False)
    type_machine=models.CharField("Machine_type", choices=machines, max_length=50, null=True, blank=False)
    date_create=models.DateField("Date_create", auto_now_add=True)
    is_activate=models.BooleanField("Active Machine", default=True)
    balance_machine=models.BigIntegerField(default= 0, null=True)