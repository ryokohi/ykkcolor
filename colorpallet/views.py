from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.views import generic
from .models import Color,ColorIndex,ColorType
from django.core import serializers
from django.http import JsonResponse



def index(request):
    context = {
      'color_list':Color.objects.all(),
      'column_list':ColorIndex.objects.all(),
      'colortype_list':ColorType.objects.all(),

    }

    return render(request,'colorpallet/color_list.html',context)


def color_search(request):
    keyword = request.GET.get('keyword')
    queryset = Color.objects.all()
    if keyword:
        queryset = queryset.filter(
        Q(name__icontains=keyword)
        )
    return render(request,'colorpallet/color_search.html',{'queryset':queryset})


def column_search(request):
    column_id =request.GET.get('column_tag')
    queryset = Color.objects.all()
    queryset = queryset.filter(
      Q(index_alphabet__exact=column_id)
    )
    select_column = ColorIndex.objects.all()
    select_column = select_column.filter(
      Q(id__exact=column_id)
    )
    data = {
      'queryset':queryset,
      'column_list':ColorIndex.objects.all(),
      'select_column':select_column
    }

    return render(request,"colorpallet/column_search.html",data)



def colortype_search(request):
    colortype_id =request.GET.get('colortype_tag')
    queryset = Color.objects.all()
    queryset = queryset.filter(
      Q(type__exact=colortype_id)
    )
    select_type = ColorType.objects.all()
    select_type = select_type.filter(
      Q(id__exact=colortype_id)
    )
    data = {
      'queryset':queryset,
      'colortype_list':ColorType.objects.all(),
      'select_type':select_type
    }
    return render(request,"colorpallet/colortype_search.html",data)





def color_confirm(request):
    color_id =request.GET.getlist('colors')
    select_color = Color.objects.filter(id__in=color_id)
    data = {
      'select_color':select_color,
    }
    return render(request,"colorpallet/color_confirm.html",data)




"""

class SelectView(generic.ListView):
    model = Color
    tamplate_name = 'colorpallet/color_select.html'

    def get_queryset(self):
        queryset = Color.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
            Q(name__icontains=keyword)
            )
        return queryset



def select(request):
    keyword = request.GET.get('keyword')
    if keyword:
        queryset = queryset.filter(
        Q(name__icontains=keyword)
        )
    return render(request,'colorpallet/color_select.html',{'queryset':queryset})
"""
