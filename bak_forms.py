import datetime
from django import forms
from django.forms import widgets
from django.forms.widgets import SelectDateWidget
from .models import cert

class CertForm(forms.ModelForm):

    class Meta:
        model = cert
        fields = ('title', 'system','created_date','expiry_date',)
        created_date = forms.DateField(
		widget=forms.widgets.SelectDateWidget())
        expiry_date = forms.DateField(
                widget=forms.SelectDateWidget(
                     empty_label=("Choose Year", "Choose Month", "Choose Day"),
                ),
        )
		


