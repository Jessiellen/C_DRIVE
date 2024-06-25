from django.views.generic import TemplateView, DeleteView, View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FileForm, FolderForm
from .models import File, Folder


def home_view(request):
    files = File.objects.filter(user=request.user)
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

class DirectoryListView(View):

    @method_decorator(login_required)
    def post(self, request, parent_id=None):
        folder = None
        if parent_id:
            folder = get_object_or_404(Folder, id=parent_id, user=request.user)

        if 'create_folder' in request.POST:
            folder_form = FolderForm(request.POST)
            if folder_form.is_valid():
                new_folder = folder_form.save(commit=False)
                new_folder.user = request.user
                if folder:
                    new_folder.parent = folder
                new_folder.save()
                return redirect('directory_list', parent_id=new_folder.parent.id if new_folder.parent else '')
            
        elif 'upload_file' in request.POST:
            file_form = FileForm(request.POST, request.FILES)
            if file_form.is_valid():
                new_file = file_form.save(commit=False)
                new_file.user = request.user
                if folder:
                    new_file.folder = folder
                new_file.save()
                return redirect('directory_list', parent_id=new_file.folder.id if new_file.folder else '')

        return redirect('directory_list', parent_id='')
    
class CreateFolderView(View):

    def get(self, request):
        form = FolderForm()
        return render(request, 'create_folder.html', {'form': form})

    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.user = request.user
            new_folder.save()
            return redirect('directory_list')  
        return render(request, 'create_folder.html', {'form': form})

@login_required
def trash_view(request):
    deleted_files = File.objects.filter(user=request.user, is_deleted=True)
    deleted_folders = Folder.objects.filter(user=request.user, is_deleted=True)
    return render(request, 'trash.html', {'deleted_files': deleted_files, 'deleted_folders': deleted_folders})

class UploadFileView(View):

    def get(self, request):
        form = FileForm()
        return render(request, 'upload_file.html', {'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.user = request.user
            new_file.save()
            return redirect('directory_list')  
        return render(request, 'upload_file.html', {'form': form})

class FileDownloadView(View):
    @method_decorator(login_required)
    def get(self, request, file_id):
        file = get_object_or_404(File, id=file_id, user=request.user)
        response = HttpResponse(file.file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={file.file.name}'
        return response

class FolderDeleteView(DeleteView):
    model = Folder
    success_url = reverse_lazy('directory_list')
    template_name = 'folder/folder_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FileDeleteView(DeleteView):
    model = File
    success_url = reverse_lazy('directory_list')
    template_name = 'file/file_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
