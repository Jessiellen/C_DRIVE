from django import forms
from .models import Folder, File

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'folder']


class DeleteFileForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Deletion")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FileUploadForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['file', 'folder']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['folder'].queryset = Folder.objects.filter(user=user)