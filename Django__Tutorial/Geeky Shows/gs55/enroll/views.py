from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

def showformdata(request):
    fm=StudentRegistration()
    return render(request, 'enroll/userregistration.html',{'form':fm})
