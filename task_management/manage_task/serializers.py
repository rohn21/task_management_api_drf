from rest_framework import serializers
from datetime import date
from manage_task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_status(self, value):
        if not value:
                value = self.instance.status if self.instance else 'pending'
            
        if self.instance and self.instance.status:
            valid_transitions = {
                'pending': ['in_progress', 'completed'],
                'in_progress': ['completed'],
                'completed': []
            }
            current_status = self.instance.status
            if value not in valid_transitions[current_status] and value != current_status:
                raise serializers.ValidationError(f"Invalid status from {current_status} to {value}")
            
        return value
        
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in past!!!")
        return value