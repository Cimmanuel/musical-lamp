from django import forms
from .models import WorkOrder
from django.core.exceptions import ValidationError

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'

    def clean(self):
        if self.cleaned_data.get('assigned_to').count() > 5:
            raise ValidationError({
                'assigned_to': 'You can\'t assign more than five workers'
            })
        return self.cleaned_data