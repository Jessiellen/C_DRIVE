# from django.urls import path
# from Drive_Docs.views import FileIndexView, FileCreateView, FileUploadView, FileDeleteView, FileDownloadView, FolderCreateView, FolderDeleteView, FolderIndexView, FolderListView

# urlpatterns = [
# #     # URLs para arquivos
# #     path('', FileIndexView.as_view(), name='file_list'),
# #     path('files/create/', FileCreateView.as_view(), name='file_create'),  
# #     path('create/', FileCreateView.as_view(), name='create_file'),  
# #     path('upload/', FileUploadView.as_view(), name='file_upload'),  
# #     path('delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),  
# #     path('download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),  

# #     # URLs para pastas
# #     path('folders/', FolderIndexView.as_view(), name='folder_list'),
# #     path('folders/<int:parent_id>/', FolderListView.as_view(), name='folder_list'),  
# #     path('folders/create/', FolderCreateView.as_view(), name='folder_create'), 
# #     path('folders/create/<int:parent_id>/', FolderCreateView.as_view(), name='folder_create_subfolder'), 
# #     path('folders/delete/<int:pk>/', FolderDeleteView.as_view(), name='folder_delete'), 
# # ]
    
from django.urls import path
from . import views
from .views import DirectoryListView, FileDownloadView, FolderDeleteView, FileDeleteView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', DirectoryListView.as_view(), name='directory_list'),
    path('create_folder/', views.CreateFolderView.as_view(), name='create_folder'),
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
    path('folders/<int:parent_id>/', DirectoryListView.as_view(), name='directory_list'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='download_file'),
    path('delete-folder/<int:folder_id>/', views.FolderDeleteView.as_view(), name='folder_delete'),
    path('files/delete/<int:pk>/', FileDeleteView.as_view(), name='delete_file'),
    path('trash/', views.trash_view, name='trash'),

]





