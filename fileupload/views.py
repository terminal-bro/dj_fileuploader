from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from .serializers import FileUploadSerializer


class FileUploadView(APIView):

    parser_classes = (MultiPartParser,FormParser)

    def get(self, request, *args, **kwargs):
        return render(request, 'file_upload.html')

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)