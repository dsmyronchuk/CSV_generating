from django.db import models
from django.contrib.auth.models import User


class Schemas(models.Model):
    ColumnName = models.CharField(max_length=255)
    User = models.ForeignKey(User,  on_delete=models.PROTECT)


class FullName(models.Model):
    ColumnName = models.CharField(max_length=100)
    Order = models.IntegerField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)


class Job(models.Model):
    ColumnName = models.CharField(max_length=100)
    Order = models.IntegerField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)


class Email(models.Model):
    ColumnName = models.EmailField(max_length=255)
    Order = models.IntegerField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)


class DomainName(models.Model):
    ColumnName = models.URLField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)


class PhoneNumber(models.Model):
    ColumnName = models.PhoneNumberField()
    Order = models.IntegerField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)


class CompanyName(models.Model):
    ColumnName = models.CharField(max_length=255)
    Order = models.IntegerField()
    schemas = models.ForeignKey('Schemas', on_delete=models.PROTECT)
