from rest_framework import serializers
from .models import SensorData

# Serializers define the API representation.
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'Location', 'Voltage_value', 'Current_value', 'author']

