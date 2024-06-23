from django.urls import path
from files.views import FileIndexView, FileCreateView, FileUploadView, FileDeleteView, FileDownloadView, FolderCreateView, FolderDeleteView, FolderIndexView

urlpatterns = [
    # URLs para arquivos
    path('', FileIndexView.as_view(), name='file_list'),  
    path('create/', FileCreateView.as_view(), name='create_file'),  
    path('upload/', FileUploadView.as_view(), name='file_upload'),  
    path('delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),  
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),  

    # URLs para pastas
    path('folders/', FolderIndexView.as_view(), name='folder_list'),  
    path('folders/create/', FolderCreateView.as_view(), name='folder_create'),  
    path('folders/delete/<int:pk>/', FolderDeleteView.as_view(), name='folder_delete'), 
]




