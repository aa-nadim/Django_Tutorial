from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm=StudentRegistration(auto_id=True, label_suffix=' ',
                           initial={'name': 'Nadim'})
    return render(request, 'enroll/userregistration.html',
                  {'form':fm})