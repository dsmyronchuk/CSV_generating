from django.db import models
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.urls import reverse
from django.utils.text import slugify


class Schemas(models.Model):
    Name = models.CharField(max_length=255, null=False)
    User = models.ForeignKey(User,  on_delete=models.PROTECT)
    ColumnSeparator = models.ForeignKey('ColumnSeparator', on_delete=models.PROTECT)
    StringCharacter = models.ForeignKey('StringCharacter', on_delete=models.PROTECT)
    Modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('schema', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class SchemasColumn(models.Model):
    Name = models.CharField(max_length=255,  null=False)
    Order = models.IntegerField(null=False)
    Schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)
    TypeColumn = models.ForeignKey('TypeColumn', on_delete=models.PROTECT,  null=False)
    min_value = models.IntegerField(blank=True, null=True)
    max_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name


class TypeColumn(models.Model):
    TypeName = models.CharField(max_length=255)

    def __str__(self):
        return self.TypeName


class DataSets(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Schemas = models.ForeignKey(Schemas, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сначала сохраняем модель
        self.slug = slugify(f"{self.Schemas}__{self.pk}")  # Затем определяем slug
        print(self.slug)

    def get_absolute_url(self):
        self.save()
        return reverse('download_file', kwargs={'filename': self.slug})


class ColumnRows(models.Model):
    DataRow = models.CharField(max_length=255)
    DataSet = models.ForeignKey(DataSets, on_delete=models.PROTECT)
    TypeColumn = models.ForeignKey('SchemasColumn', on_delete=models.PROTECT)

    def __str__(self):
        return self.DataRow[:20]


class ColumnSeparator(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class StringCharacter(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
