import datetime
from django import forms
from django.forms import widgets
#from django.forms.widgets import SelectDateWidget
#from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from .models import cert

class CertForm(forms.ModelForm):

    class Meta:
        model = cert
        #fields = ('title', 'system','created_date','expiry_date',)
        fields = '__all__'
        widgets = {
           'created_date': widgets.AdminDateWidget,
           'expiry_date': widgets.AdminDateWidget,
        }
