from django import forms
from .models import Store
class StoreForm(forms.Form):
    #The name of attribute must be align with the name in HTML
    name = forms.CharField(max_length=10,required= True)
    location = forms.CharField(max_length=100,required= True)  
    manager_select = forms.CharField( max_length=20,required= True)
class StoreUpdateForm(forms.Form):
    #The name of attribute must be align with the name in HTML
    input_storename = forms.CharField(max_length=10,required= True)
    input_storelocation = forms.CharField(max_length=100,required= True)  
    manager_select = forms.CharField( max_length=20,required= True)
   