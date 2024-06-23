from django.views.generic import TemplateView, DeleteView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import FileForm, FolderForm
from .models import File, Folder
# Create your views here.

class FolderIndexView(TemplateView):
    template_name = 'folder/folder_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folders'] = Folder.objects.filter(user=self.request.user)
        return context

class FolderCreateView(View):
    def get(self, request):
        form = FolderForm()
        return render(request, 'folder/create_folder.html', {'form': form})

    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.user = request.user
            new_folder.save()
            return redirect('folder_list')
        return render(request, 'folder/create_folder.html', {'form': form})

class FolderDeleteView(DeleteView):
    model = Folder
    success_url = reverse_lazy('folder_list')
    template_name = 'folder/folder_delete.html'

class FileIndexView(TemplateView):
    template_name = 'file/file_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = File.objects.filter(user=self.request.user)
        return context

class FileCreateView(View):
    def get(self, request):
        form = FileForm()
        return render(request, 'file/create_file.html', {'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.user = request.user
            new_file.save()
            return redirect('file_list')
        return render(request, 'file/create_file.html', {'form': form})

class FileDeleteView(DeleteView):
    model = File
    success_url = reverse_lazy('file_list')
    template_name = 'file/file_delete.html'

class FileDownloadView(View):
    def get(self, request, file_id):
        file = get_object_or_404(File, pk=file_id, user=request.user)
        response = HttpResponse(file.file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={file.title}'
        return response
    
class FileUploadView(View):
    def get(self, request):
        form = FileForm()
        return render(request, 'file/file_upload.html', {'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            return redirect('file_list') 

        return render(request, 'file/file_upload.html', {'form': form})