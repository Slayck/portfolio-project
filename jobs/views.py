from django.http import HttpResponse
from django.shortcuts import render
import operator
from .models import Job

#for regerence in case you want to write the whole page in it
#def hello(request):
#    return HttpResponse("<h1>Hello World!</h1>") #Code is inside of it

def home(request):
    jobs = Job.objects
    '''for jobx in jobs:
        print(jobx['title'])'''
    return render(request,"jobs/home.html",{"jobs":jobs}) #Code is rendering you into a full html page
