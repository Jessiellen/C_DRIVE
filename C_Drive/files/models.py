from django.db import models
from django.conf import settings

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='subfolders', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name
    
    class Meta:  
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
        ordering = ['id']

class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title
    
    class Meta:  
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ['id']
