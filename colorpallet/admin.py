from django.contrib import admin
from .models import Color,ColorType,ColorIndex
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget



admin.site.register(ColorType)
admin.site.register(ColorIndex)


class ColorResource(resources.ModelResource):

    class Meta:
        model = Color
        skip_unchanged = False
        report_skipped = False
        import_id_fields= ['name']
        fields = ('name','color_code','index_alphabet','index_number','type')


@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource
