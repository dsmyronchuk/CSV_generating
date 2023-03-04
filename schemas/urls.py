from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', DateSchemas.as_view(), name='DateSchemas'),
    path('new_schemas/', new_schemas, name='NewSchemas'),
    path('save_schema/', SaveSchema.as_view(), name='SaveSchema'),
    path('schema/<int:pk>/', ShowSchema.as_view(), name='schema'),
    path('generate_data/', GenerateData.as_view(), name='GenerateData'),
    path('download_csv/<str:schema_name>/<int:dataset_id>/', download_file, name='download_file')
]
