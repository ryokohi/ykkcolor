from django.urls import path
from . import views

app_name = 'colorpallet'

urlpatterns = [
    path('',views.index,name='index'),
    path('color_search/',views.color_search, name='color_search'),
    path('column_search/',views.column_search, name='column_search'),
    path('colortype_search/',views.colortype_search,name='colortype_search'),
    path('color_confirm/',views.color_confirm,name='color_confirm'),
]
