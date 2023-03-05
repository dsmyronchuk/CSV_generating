import csv
import os

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from CSV_generating import settings
from schemas.models import *
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from faker import Faker
import json
import pandas as pd


class DateSchemas(ListView):
    template_name = 'schemas/Data_schemas.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        id_user = self.request.user.id
        return Schemas.objects.filter(User=id_user)


def new_schemas(request):
    type_column = TypeColumn.objects.all()
    separator = ColumnSeparator.objects.all()
    character = StringCharacter.objects.all()
    user_id = request.user.id

    context = {'type_column': type_column, 'separator': separator, 'character': character, 'user_id': user_id}
    return render(request, 'schemas/New_schemas.html', context)


class SaveSchema(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        column_separator = ColumnSeparator.objects.get(Name=content['columnSeparator'])
        string_character = StringCharacter.objects.get(Name=content['stringCharacter'])
        user_id = User.objects.get(id=content['userId'])

        new_schema = Schemas(Name=content['nameSchema'],
                             User=user_id,
                             ColumnSeparator=column_separator,
                             StringCharacter=string_character)
        new_schema.save()

        for k, v in content['allColumns'].items():
            type_column = TypeColumn.objects.get(TypeName=v[0])
            if str(type_column) != 'Integer':
                SchemasColumn(Name=k,
                              Order=v[1],
                              TypeColumn=type_column,
                              Schemas=new_schema).save()
            else:
                SchemasColumn(Name=k,
                              Order=v[1],
                              TypeColumn=type_column,
                              Schemas=new_schema,
                              min_value=v[2],
                              max_value=v[3]).save()

        return JsonResponse({'status': 'ok'})


class ShowSchema(DetailView):
    model = Schemas
    template_name = 'schemas/Show_schema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schema_columns = self.object.schemascolumn_set.all().order_by('Order')
        data_sets = self.object.datasets_set.all()
        context['schema_columns'] = schema_columns
        context['data_sets'] = data_sets
        return context


class GenerateData(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        count = content['amountRows']
        schema = Schemas.objects.get(pk=content['schemaID'])
        new_data_set = DataSets(Schemas=schema)
        new_data_set.save()

        all_columns = schema.schemascolumn_set.all().order_by('Order')

        fake = Faker()
        fake_dict = {
            'Domain Name': fake.domain_name,
            'Phone Number': fake.phone_number,
            'Company Name': fake.company,
            'Email': fake.email,
            'Job': fake.job,
            'Full Name': fake.name,
            'Integer': fake.random_int,
        }

        separator_dict = {
            'Tab (' ')': '\t',
            'semicolon (;)': ';',
            'Comma (,)': ',',
        }

        quoter_dict = {
            "Single-quote (')": "'",
            'Double-quote (")': '"',
        }

        # generate random value and save to db
        rows_dict = {}
        for row in range(int(count)):
            for column in all_columns:
                if str(column.TypeColumn) != 'Integer':
                    fake_value = fake_dict[str(column.TypeColumn)]()
                else:
                    fake_value = fake_dict[str(column.TypeColumn)](min=int(column.min_value), max=int(column.max_value))

                ColumnRows(DataRow=fake_value,
                           DataSet=new_data_set,
                           TypeColumn=column).save()

                rows_dict.setdefault(str(column), []).append(fake_value)

        # create csv file
        selected_quoter = str(schema.StringCharacter)
        selected_separator = str(schema.ColumnSeparator)

        quoting = quoter_dict[selected_quoter]
        separator = separator_dict[selected_separator]

        df = pd.DataFrame.from_dict(rows_dict)
        file_path = os.path.join(settings.STATIC_ROOT, 'csv_files', f'{schema.Name}_dataset_{new_data_set.pk}.csv')
        df.to_csv(file_path, sep=separator, quotechar=quoting, quoting=csv.QUOTE_MINIMAL, index=False)

        return JsonResponse({'schema_name': schema.Name, 'data_set_pk': new_data_set.pk})


def download_file(request, schema_name, dataset_id):
    filename = f'{schema_name}_dataset_{dataset_id}.csv'
    file_path = os.path.join(settings.STATIC_ROOT, 'csv_files', filename)
    return FileResponse(open(file_path, 'rb'))
