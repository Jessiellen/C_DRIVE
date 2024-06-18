from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        pass

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  
        related_query_name='user',
    )