from django.views.generic import DeleteView, View
from .forms import FileForm, FolderForm, DeleteFileForm, FileUploadForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import File, Folder
from django.contrib import messages
from django.utils.text import slugify
import zipfile
import io
import os


def home_view(request):
    files = File.objects.filter(user=request.user,folder__isnull=True).all()
    folders = Folder.objects.filter(user=request.user, parent__isnull=True)
    folder_form = FolderForm()
    file_form = FileForm()
    
    context = {
        'files': files,
        'folders': folders,
        'folder_form': folder_form,
        'file_form': file_form,
    }
    return render(request, 'home.html', context)

# def folder_view(request, folder_id):
#     folder = get_object_or_404(Folder, id=folder_id, user=request.user)
#     subfolders = folder.subfolders.all()
#     files = folder.files.all()
    
#     context = {
#         'folder': folder,
#         'subfolders': subfolders,
#         'files': files,
#     }
    
#     return render(request, 'folder/folder_view.html', context)

class FolderView(View):
    def get(self, request, folder_id):
        folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        subfolders = Folder.objects.filter(parent=folder, user=request.user)
        files = File.objects.filter(folder=folder, user=request.user)
        form = FileUploadForm(user=request.user)
        return render(request, 'folder/folder_view.html', {
            'folder': folder,
            'subfolders': subfolders,
            'files': files,
            'form': form
        })

    def post(self, request, folder_id):
        folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        form = FileUploadForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            file = form.cleaned_data['file']
            file = form.cleaned_data['file']
            file = File.objects.create(file=file, folder=folder, user=request.user)
            return redirect('folder_view', folder_id=folder_id)
        else:
            subfolders = Folder.objects.filter(parent=folder, user=request.user)
            files = File.objects.filter(folder=folder, user=request.user)
            return render(request, 'folder/folder_view.html', {
                'folder': folder,
                'subfolders': subfolders,
                'files': files,
                'form': form
})
        
class CreateFolderView(View):
    def get(self, request, parent_id=None):
        parent_folder = None
        if parent_id:
            parent_folder = get_object_or_404(Folder, id=parent_id, user=request.user)
        form = FolderForm(initial={'parent': parent_folder})
        return render(request, 'folder/create_folder.html', {'form': form, 'parent_id': parent_id})

    def post(self, request, parent_id=None):
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.user = request.user
            if parent_id:
                parent_folder = get_object_or_404(Folder, id=parent_id, user=request.user)
                new_folder.parent = parent_folder
            new_folder.save()
            return redirect('home2')
        return render(request, 'folder/create_folder.html', {'form': form, 'parent_id': parent_id})
    
class FolderDownloadView(View):
    def get(self, request, folder_id):
        folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        
        # Armazena o conteúdo em zip
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zip_file:
            self.add_folder_to_zip(folder, zip_file)
        
        #download do arquivo zip
        zip_filename = f"{slugify(folder.name)}.zip"
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'
        
        return response
    
    def add_folder_to_zip(self, folder, zip_file, parent_path=''):
        # Adiciona arquivos ao zip
        for file in folder.files.all():
            file_path = os.path.join(parent_path, file.file.name.split('/')[-1])
            zip_file.writestr(file_path, file.file.read())
        
        # Adiciona subpastas ao arquivo zip
        for subfolder in folder.subfolders.all():
            subfolder_path = os.path.join(parent_path, subfolder.name)
            self.add_folder_to_zip(subfolder, zip_file, subfolder_path)

class FolderDeleteView(DeleteView):
    model = Folder
    success_url = reverse_lazy('home2')
    template_name = 'folder/folder_delete.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
# class UploadFileView(View):
#     def get(self, request):
#         form = FileUploadForm(user=request.user) 
#         return render(request, 'file/file_upload.html', {'form': form})

#     def post(self, request):
#         form = FileUploadForm(request.user, request.POST, request.FILES)  
#         if form.is_valid():
#             file = form.save(commit=False)
#             file.user = request.user  
            
#             folder_id = form.cleaned_data['folder'].id
#             folder = get_object_or_404(Folder, id=folder_id, user=request.user)
#             file.folder = folder  
            
#             file.save()
#             messages.success(request, 'File uploaded successfully.')
#             return redirect('home2')
#         else:
#             messages.error(request, 'Error uploading file.')
#             return render(request, 'file/file_upload.html', {'form': form})
class UploadFileView(View):
    def get(self, request, folder_id=None):
        folder = None
        if folder_id:
            folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        form = FileUploadForm(user=request.user)
        return render(request, 'folder/folder_view.html', {'form': form, 'folder': folder})

    def post(self, request, folder_id=None):
        folder = None
        if folder_id:
            folder = get_object_or_404(Folder, id=folder_id, user=request.user)
        form = FileUploadForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            file_model = form.save(commit=False)
            file_model.user = request.user
            if folder:
                file_model.folder = folder
            file_model.name = file_model.file.name
            file_model.save()
            if folder_id:
                return redirect('folder_view', folder_id=folder_id)
            else:
                return redirect('home2')
        return render(request, 'folder/folder_view.html', {'form': form, 'folder': folder})
        
class FileDownloadView(View):
    def get(self, request, file_id):
        # Busca o File pleo ID/usuário atual
        file = get_object_or_404(File, id=file_id, user=request.user)
        
        # mensagem para receber o download
        response = HttpResponse(file.file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
        
        return response

class FileDeleteView(View):
    def get(self, request, file_id):
        file = get_object_or_404(File, id=file_id)
        return render(request, 'file/file_delete.html', {'file': file})

    def post(self, request, file_id):
        file = get_object_or_404(File, id=file_id)
        file.delete()
        return redirect('home2') 