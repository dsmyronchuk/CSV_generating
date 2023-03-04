from django.contrib import admin
from schemas.models import *
from users.models import *


class TypeColumnAdmin(admin.ModelAdmin):
    list_display = ('TypeName', )
    list_display_link = ('TypeName', )
    search_fields = ('TypeName', )


class SchemasAdmin(admin.ModelAdmin):
    list_display = ('Name', 'User', 'ColumnSeparator', 'StringCharacter', 'Modified', )
    list_display_link = ('Name', 'User', 'ColumnSeparator', 'StringCharacter', 'Modified', )
    search_fields = ('Name', 'User', 'ColumnSeparator', 'StringCharacter', 'Modified', )


class SchemasColumnAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Order', 'Schemas', 'TypeColumn', )
    list_display_link = ('Name', 'Order', 'Schemas', 'TypeColumn', )
    search_fields = ('Name', 'Order', 'Schemas', 'TypeColumn', )


class DataSetsAdmin(admin.ModelAdmin):
    list_display = ('created', 'Schemas', )
    list_display_link = ('created', 'Schemas', )
    search_fields = ('created', 'Schemas',)


class ColumnRowsAdmin(admin.ModelAdmin):
    list_display = ('DataRow', 'DataSet', 'TypeColumn', )
    list_display_link = ('DataRow', 'DataSet', 'TypeColumn', )
    search_fields = ('DataRow', 'DataSet', 'TypeColumn', )


class ColumnSeparatorAdmin(admin.ModelAdmin):
    list_display = ('Name', )
    list_display_link = ('name', )
    search_fields = ('name', )


class StringCharacterAdmin(admin.ModelAdmin):
    list_display = ('Name', )
    list_display_link = ('name', )
    search_fields = ('name', )


admin.site.register(TypeColumn, TypeColumnAdmin)
admin.site.register(Schemas, SchemasAdmin)
admin.site.register(SchemasColumn, SchemasColumnAdmin)
admin.site.register(ColumnRows, ColumnRowsAdmin)
admin.site.register(DataSets, DataSetsAdmin)
admin.site.register(ColumnSeparator, ColumnSeparatorAdmin)
admin.site.register(StringCharacter, StringCharacterAdmin)
