from django.http import HttpResponse
from django.shortcuts import render
import operator
from .models import Blog

#for regerence in case you want to write the whole page in it
#def hello(request):
#    return HttpResponse("<h1>Hello World!</h1>") #Code is inside of it

def home(request):
    blogItems = Blog.objects
    return render(request,"blog/home.html",{"blogItems":blogItems}) #Code is rendering you into a full html page
