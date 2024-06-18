from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Files
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from somewhere import handle_uploaded_file

# Create your views here.

class IndexView(TemplateView):
    template_name = 'files/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        return context

class UploadView(TemplateView):
    template_name = 'files/upload.html'


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)