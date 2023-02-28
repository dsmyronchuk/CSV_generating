from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('home/', DateSchemas.as_view(), name='DateSchemas'),
    ]
