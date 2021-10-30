from django.urls import path
from .views import *

app_name = 'clientes'

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name="upload_file")
]
