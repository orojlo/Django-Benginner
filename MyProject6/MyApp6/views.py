from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'MyApp6/index.html')

def other(request):
    return render(request,'MyApp6/other.html')

def relative(request):
    return render(request,'MyApp6/relative_url_templates.html')
