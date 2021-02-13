from django import  forms
class StudentRegistration(forms.Form):
    name=forms.CharField(initial="Nadim", help_text="in this field,you can write 30 char.")

