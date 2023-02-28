from django.shortcuts import render
from django.views.generic import ListView
from schemas.models import *


class DateSchemas(ListView):
    template_name = 'schemas/Data_schemas.html'
    queryset = Schemas.objects.all()
