from rest_framework import serializers
from .models import Worker, WorkOrder

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class WorkOrderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = WorkOrder
        fields = '__all__'
    
    def validate_assigned_to(self, value):
        if len(value) > 5:
            raise serializers.ValidationError('You can only assign 5 workers!')
        return value