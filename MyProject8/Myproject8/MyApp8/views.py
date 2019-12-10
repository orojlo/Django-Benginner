from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView)
from . import models
#from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'MyApp/school_detail.html'














# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Basic Injection!'
#         return context


# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based View Added")
