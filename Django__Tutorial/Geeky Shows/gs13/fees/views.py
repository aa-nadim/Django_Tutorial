from django.shortcuts import render

#tutorial of for loop
def fees_django(request):
    data = {'stu1':{'name':'nadim','roll':101},
            'stu2':{'name':'rakib','roll':102},
            'stu3': {'name': 'sakib', 'roll': 103},
            'stu4': {'name': 'aakib', 'roll': 104},
           }

    return render(request, 'fees/feesone.html',
                  {'data':data})

#tutorial of if condition
def fees_python(request):
    a='Django'
    b=5
    django_details = {'nm': a, 'st':b}
    return render(request, 'fees/feestwo.html',
                  django_details)


