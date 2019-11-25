from django.shortcuts import render
from MyApp4.models import User
# Create your views here.

def index(request):
    return render(request,'MyApp4/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'MyApp4/users.html',context=user_dict)
