from django.core import validators
from django import  forms
from .models import User

class StudentRegistration(forms.ModelForm):
   class Meta:
      model=User
      fields=['name', 'email', 'password']
      labels={'name':'Enter Name','email':'Enter Email',
              'password':'Enter Passwoed'}
      widgets={'password':forms.PasswordInput}
