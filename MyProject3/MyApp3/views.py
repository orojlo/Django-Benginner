from django.shortcuts import render
from django.http import HttpResponse
from MyApp3.models import Topic,Webpage,AccressRecord

# Create your views here.

def index(request):
    webpages_list = AccressRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request,'MyApp3/index.html',context=date_dict)
