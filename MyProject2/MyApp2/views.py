from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_cn':"Hello From MyApp2"}
    return render(request,'MyApp2/index.html',context=my_dict)
