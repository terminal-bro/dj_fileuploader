from django.db import models

# Create your models here.


class FileUploadModel(models.Model):
    
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank= True)

    


