from django import forms
from . models import Userdetail
from django.core.validators import RegexValidator
class ResponseForm(forms.Form):
   name = forms.CharField(max_length=100)
   address = forms.CharField(max_length=100)
 
   phone = forms.CharField(max_length=10,min_length=10)
   Query = forms.CharField(widget=forms.Textarea)
   Query_date = forms.DateTimeField()
    # class Meta:
    #     model = Userdetail
    #     fields ='__all__'

    