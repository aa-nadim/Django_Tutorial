from django import  forms
class StudentRegistration(forms.Form):
   name = forms.CharField(min_length=5,max_length=10, strip=False,
      empty_value='nadim', error_messages={'required':'Enter Your Name'})
   roll=forms.IntegerField()
   price=forms.DecimalField()
   rate=forms.FloatField(min_value=5,max_value=40)
   comment=forms.SlugField()

   email=forms.EmailField()
   website = forms.URLField()
   password=forms.CharField(widget=forms.PasswordInput)
   description=forms.CharField(widget=forms.Textarea)
   feedback=forms.CharField(
                            widget=forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))
   notes=forms.CharField(widget=forms.Textarea(attrs={'row':3,'cols':50}))
   agree=forms.BooleanField(label_suffix=' ', label='I Agree')



