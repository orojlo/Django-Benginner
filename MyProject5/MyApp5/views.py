from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'MyApp5/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        # DO Somthing Code
        print("Validation Success!")
        print("NAME: "+form.cleaned_data['name'])
        print("EMAIL: "+form.cleaned_data['email'])
        print("TEXT: "+form.cleaned_data['text'])

    return render(request,'MyApp5/forms.html',{'form':form})
