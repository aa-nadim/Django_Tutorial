from django.shortcuts import render
from MyApp.models import Student

def studentinfo(request):
    stud = Student.objects.all()
    print('Myoutput', stud)
    return render(request,'MyApp/studetails.html',{'stu': stud})

