from rest_framework import serializers
from .models import WheelSpecificationForm

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    formNumber = serializers.CharField(source='form_number')
    submittedBy = serializers.CharField(source='submitted_by')
    submittedDate = serializers.DateField(source='submitted_date')

    class Meta:
        model = WheelSpecificationForm
        fields = ['id', 'formNumber', 'submittedBy', 'submittedDate', 'fields', 'status']        