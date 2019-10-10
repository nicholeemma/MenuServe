from django import forms
from .models import Store,Manager,Employee,Order,Menu,Document
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#validation for gender, can only be female or male
def validate_gender(value):
    list =["male","Female","female","Male","M","m","F","f"]
    
    if not (value in list):
        raise ValidationError(
            _('%(value)s should be male or female'),
            params={'value': value},
        )

# convert user input to standard form
class GenderField(forms.CharField):
    def to_python(self, value):
        list_m = ["male","Male","M","m"]
        list_f = ["Female","female","F","f"]
        if value in list_m:
            return "M"
        if value in list_f:
            return "F"
        return value.lower()

class StoreForm(forms.Form):
    #The name of attribute must be align with the name in HTML
    name = forms.CharField(max_length=10,required= True,help_text='10 characters max.')
    location = forms.CharField(max_length=100,required= True)  
    manager_select = forms.CharField( max_length=20,required= True)

class StoreUpdateForm(forms.Form):
    #The name of attribute must be align with the name in HTML
    input_storename = forms.CharField(max_length=10,required= True)
    input_storelocation = forms.CharField(max_length=100,required= True)  
    manager_select = forms.CharField( max_length=20,required= True)

class ManagerForm(forms.Form):
    name = forms.CharField(max_length=20,required= True)
    gender = GenderField(validators=[validate_gender],required= True)  

class ManagerUpdateForm(forms.Form):
    input_managername = forms.CharField(max_length=20,required= True)
    input_managergender = GenderField(validators=[validate_gender],required= True) 

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=20,required= True)

class EmployeeUpdateForm(forms.Form):
    input_employeename = forms.CharField(max_length=20,required= True)

   