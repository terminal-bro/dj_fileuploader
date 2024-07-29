from rest_framework import serializers
from .models import FileUploadModel


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = '__all__'

        