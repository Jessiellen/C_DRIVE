from django.urls import path
from .views import FileDownloadView, FolderDeleteView, FileDeleteView, FolderDownloadView, UploadFileView, FolderView
from . import views

urlpatterns = [
    path('', views.home_view, name='home2'),
    path('create_folder/', views.CreateFolderView.as_view(), name='create_folder'),
    path('create_folder/<int:parent_id>/', views.CreateFolderView.as_view(), name='create_subfolder'),
    path('folder/delete/<int:pk>/', FolderDeleteView.as_view(), name='folder_delete'),
    path('folder/<int:folder_id>/', FolderView.as_view(), name='folder_view'),
    path('download/folder/<int:folder_id>/', FolderDownloadView.as_view(), name='folder_download'),
    path('upload/', views.UploadFileView.as_view(), name='file_upload'),
    path('file/download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),
    path('file/delete/<int:file_id>/', FileDeleteView.as_view(), name='file_delete'),
    path('upload/<int:folder_id>/', UploadFileView.as_view(), name='upload_file_to_folder'),

]





