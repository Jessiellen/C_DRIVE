from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subfolders', on_delete=models.CASCADE)

    def get_absolute_url(self):
        if self.parent:
            return reverse('folder_list', kwargs={'parent_id': self.parent.id})
        else:
            return reverse('folder_list')
        
    def __str__(self):
        return self.name
    
    class Meta:  
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
        ordering = ['id']

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files', default=1, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.file.name
    
    class Meta:  
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ['id']

