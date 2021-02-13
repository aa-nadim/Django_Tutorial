from django import  forms
class StudentRegistration(forms.Form):
   name = forms.CharField()
   email=forms.EmailField()
   password=forms.ChairField(widget=forms.PasswordInput)




