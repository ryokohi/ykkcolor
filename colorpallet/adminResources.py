from import_export import resources
from .models import Color

class ColorResource(resources.ModelResource):

    class Meta:
        model = Color
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('name','color_code','index_alphabet','index_number')
