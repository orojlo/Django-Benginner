from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Index Text")
def MyApp1(request):
    my_dict = {'insert_me':"Now I am coming from MyApp1/index.html!"}
    return render(request,'MyApp1/index.html',context=my_dict)
def MyApp2(request):
    you_dict = {'you_dict':"Its Just for test My Skill"}
    return render(request,'MyApp2/index.html',context=you_dict)
