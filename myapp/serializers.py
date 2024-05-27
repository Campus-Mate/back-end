from rest_framework import serializers
from .models import IDRecord

class IDRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDRecord
        fields = ['id_value', 'created_at', 'content', 'category','created_at']
