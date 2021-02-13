from django.core import validators
from django import  forms


class StudentRegistration(forms.Form):
   error_css_class='error'
   required_css_class='required'
   name = forms.CharField(error_messages={'required':'Enter Your Name'})

   email=forms.EmailField(error_messages={'required':'Enter Your Email'})

   password=forms.EmailField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'})