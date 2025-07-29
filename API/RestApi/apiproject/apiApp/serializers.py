
from rest_framework import serializers
from apiApp.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

    def create(self, validated_data):
        latest_roll = StudentModel.objects.order_by(-roll)
        student_data = StudentModel.objects.create(**validated_data)
        student_data.roll