from django.core import validators
from django import  forms
from .models import User

class StudentRegistration(forms.ModelForm):
   class Meta:
      model=User
      fields=['name', 'email', 'password']
      labels={'name':'Enter Name','email':'Enter Email','password':'Enter Passwoed'}
      error_messages={
         'name':{'required':'name is needed'},
         'password': {'required': 'password is needed'}
      }
      widgets={
         'password':forms.PasswordInput,
         'name':forms.TextInput(attrs={'class':'myclass',
                                       'placeholder':'write here your name'})
      }