from django.shortcuts import render
from datetime import datetime

def learn_django(request):
    cname = 'Django'
    duration = '4 Months'
    seats = 10
    d = datetime.now()
    django_details = {'nm':cname,'du':duration,'st':seats,'dt':d}
    return render(request, 'course/courseone.html',
                  django_details)


def learn_python(request):
    a = 56.24311
    b=56.0000
    c=56.52000
    d = datetime.now()
    django_details = {'p1':a, 'p2': b, 'p3': c}
    return render(request, 'course/coursetwo.html',
                  django_details)


