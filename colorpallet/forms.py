from django import forms
from .models import ColorIndex
from .widgets import CustomCheckboxSelectMultiple


class SearchForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
      label='絞り込み',
      required = False,
      queryset = ColorIndex.objects.order_by('index_alphabet'),
      widget = CustomCheckboxSelectMultiple,
    )
