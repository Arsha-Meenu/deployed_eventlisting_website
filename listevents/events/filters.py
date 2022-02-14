from unicodedata import category
import django_filters
from django_filters.widgets import RangeWidget
from django.utils.translation import gettext as _
from django import forms
from .models import Event

class EventFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(field_name="categories",lookup_expr='icontains',label='Category'
            ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : "Search by Category..."}))
   
   
    start_date = django_filters.DateFilter(field_name="start_date",label='Start Date',
                widget=forms.DateInput(attrs={"type":"date",'class':'form-control',}))

    end_date = django_filters.DateFilter(field_name="end_date",label='End Date',widget=forms.DateTimeInput(
                 format='%d/%m/%Y %H:%M', attrs={'type': 'date','class':'form-control',}))



        
    class Meta:
        model = Event
        fields = ['categories', 'start_date','end_date']