from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

def regi(request):
    messages.info(request,'Now you can login')
    messages.success(request, 'messages are updated')
    messages.warning(request, 'This is warning')
    messages.error(request, 'This is error')
    fm=StudentRegistration()
    return render(request, 'enroll/userregistration.html',
                  {'form':fm})

