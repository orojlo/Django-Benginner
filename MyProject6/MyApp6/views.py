from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello AmirHosein','number':100}
    return render(request,'MyApp6/index.html',context_dict)

def other(request):
    return render(request,'MyApp6/other.html')

def relative(request):
    return render(request,'MyApp6/relative_url_templates.html')
