from django.urls import path, include
from . import views
from .views import IndexView, UploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='files_index'),
    path('upload/', UploadView.as_view(), name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
