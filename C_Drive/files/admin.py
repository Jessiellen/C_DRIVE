from django.contrib import admin
from .models import File, Folder


# Register your models here.
from django.contrib import admin
from files.models import File, Folder

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'user')
    search_fields = ('name',)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'folder', 'user')
    search_fields = ('title',)

# admin.site.register(File)
# admin.site.register(Folder)