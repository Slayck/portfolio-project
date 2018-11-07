from django.http import HttpResponse
from django.shortcuts import render
import operator

#for regerence in case you want to write the whole page in it
#def hello(request):
#    return HttpResponse("<h1>Hello World!</h1>") #Code is inside of it

def home(request):
    return render(request,"blog/home.html",{"welcome":"Welcome to your Dragon World"}) #Code is rendering you into a full html page
