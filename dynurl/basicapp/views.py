from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def show_details(request, my_id):
#     # whenever no path converter provided, it takes in str by default converter
#     return render(request, 'show.html', context={'student':my_id})



def home(request):
    return render(request,'home.html')

def index(request):
    return HttpResponse('hey there')

def show_details(request, my_id):
    # give conditions of parameters to change output
    if my_id==1:
        student = {'id':my_id, 'name':'Arvind', 'marks':100, 'sub':'Physics'}
    # give conditions of parameters to change output
    if my_id==2:
        student = {'id':my_id, 'name':'Ashwin', 'marks':98, 'sub':'Botany'}
    # give conditions of parameters to change output
    if my_id==3:
        student = {'id':my_id, 'name':'Srinivas', 'marks':95, 'sub':'Psychology'}
    # give conditions of parameters to change output
    if my_id==4:
        student = {'id':my_id, 'name':'Rahul', 'marks':60, 'sub':'Chemistry'}
    if my_id==5:
        student = {'id':my_id, 'name':'Gopalan', 'marks':72, 'sub':'Applied Physics'}
    
    return render(request, 'show.html', context=student)
