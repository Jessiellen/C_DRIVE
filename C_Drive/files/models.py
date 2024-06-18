from django.db import models
from django.conf import settings

# Create your models here.

class Type(models.Model):
    nome = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self): 
        return self.nome
    
    class Meta:  
        verbose_name = 'Type'
        verbose_name_plural = 'Type'
        ordering = ['id']

class File(models.Model):
    title = models.CharField(max_length=200)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    type = 

#type para para me dAr a hierarquia 
    def __str__(self):
        return self.title