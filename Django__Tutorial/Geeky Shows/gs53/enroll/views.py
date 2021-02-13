from django.shortcuts import render

def home(request, check):

    return render(request, 'enroll/home.html', {'ch':check})

#def show_details(request,my_id):
 #   student={'id':my_id}
  #  return render(request, 'enroll/show.html',student)

def show_details(request,my_id):
    if my_id==1:
        student = {'id': my_id, 'name':'Rohan'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Nadim'}
    if my_id == 3:
         student = {'id': my_id, 'name': 'Akib'}
    return render(request, 'enroll/show.html',student)

def show_subdetails(request,my_id,my_subid):
    if my_id==1 and my_subid==5:
        student = {'id': my_id, 'name':'Rohan', 'info':'Sub Details'}
    if my_id == 2 and my_subid==6:
        student = {'id': my_id, 'name': 'Nadim', 'info':'Sub Details'}
    if my_id == 3 and my_subid==7:
         student = {'id': my_id, 'name': 'Akib', 'info':'Sub Details'}
    return render(request, 'enroll/show.html',student)