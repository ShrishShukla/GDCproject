import django_tables2 as tables
from .models import SensorData

class SensorDataTable(tables.Table):
    class Meta:
        model = SensorData
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'Location', 'Voltage_value', 'Current_value' , 'date_posted' )