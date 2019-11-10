from django import forms
from .models import Store,Manager,Employee,Order,Menu,Document
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
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
    #manager_select = forms.CharField( max_length=20,required= True)

class ManagerForm(forms.Form):
    #name = forms.CharField(max_length=20,required= True)
    gender = GenderField(validators=[validate_gender],required= True)  

class ManagerUpdateForm(forms.Form):
    #input_managername = forms.CharField(max_length=20,required= True)
    input_managergender = GenderField(validators=[validate_gender],required= True) 

# class EmployeeForm(forms.Form):
#     name = forms.CharField(max_length=20,required= True)

#class EmployeeUpdateForm(forms.Form):
    #input_employeename = forms.CharField(max_length=20,required= True)

class MenuForm(forms.Form):
    name_of_cuisine = forms.CharField(max_length=30,required= True)
    id_for_dish = forms.CharField(max_length=4,required= True)
    price = forms.IntegerField(min_value=0, max_value=1000,required= True)
    menu_select = forms.CharField(max_length=10,required= True)
    description = forms.CharField(max_length=100,required= True)
    #myfile = forms.FileField()

class MenuUpdateForm(forms.Form):
    input_menuname_of_cuisine = forms.CharField(max_length=30,required= True)
    input_menuid_for_dish = forms.CharField(max_length=4,required= True)
    input_menuprice = forms.IntegerField(min_value=0, max_value=1000,required= True)
    menu_select = forms.CharField(max_length=10,required= True)
    input_menudescription = forms.CharField(max_length=100,required= True)
    #myfile = forms.FileField()

class OrderForm(forms.Form):
    # class Meta:
    #     model = Order
    #     fields = [
    #         'desk_no',
    #         'name_of_cuisine',
    #         'status',
    #         'time',
    #         'amount',
    #         'price',
    #         'store',
    #         'order_user',
           
    #     ]
    desk_no = forms.CharField(max_length=4,required= True)
    amount = forms.IntegerField(min_value=1, max_value=1000,required= True)
    menu_select = forms.CharField(max_length=30,required= True)
    store_select = forms.CharField(max_length=30,required= True)

class OrderUpdateForm(forms.Form):
    input_desk_no = forms.CharField(max_length=4,required= True)
    input_amount = forms.IntegerField(min_value=1, max_value=1000,required= True)

# class UserForm(forms.Form):
#     username = forms.CharField(label='user name',max_length=100,required= True)
#     password1 = forms.CharField(label='psd',widget=forms.PasswordInput(),required= True)
#     password2 = forms.CharField(label='confirm psd',widget=forms.PasswordInput(),required= True)
#     email = forms.EmailField(label='email')
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 200,
                               label = 'Username')
    first_name = forms.CharField(max_length = 200,
                                 label='First Name')
    last_name = forms.CharField(max_length = 200,
                                label = 'Last Name')
    password = forms.CharField(max_length = 200,
                                label='Password',
                                widget = forms.PasswordInput())
    confirm_password = forms.CharField(max_length = 200,
                                label='Confirm password',
                                widget = forms.PasswordInput())
    email = forms.EmailField(max_length=200,
                             label='Email',
                             widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # self.fields['username'].error_messages = {'required': 'username required'}
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} cannot be empty!'.format(
                fieldname=field.label)}
            field.widget.attrs.update({'class': 'input-text'})
        # self.fields['username'].widget.attrs.update({'class': 'input-text'})

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Confirm password does not match!")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")
        return username


   