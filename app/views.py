from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import View
from app.forms import *

#FBV-FUNCTION BASED VIEW
#CBV-CLASS BASED VIEW

#Function based view returning string

def fbv_string(request):
    return HttpResponse('I AM JUNAID AKHIF')

#class based view returning string
class cbv_string(View):
    def get(self,request):
        return HttpResponse('I AM JUNAID')
    
#Function based view returning HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')

#class based view returning HTML page

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    
#HOLDING forms by using FBV

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        return HttpResponse('DATA INSERTED SUCCESSFULLY')

    return render(request,'fbv_form.html',d)

#HOLDING forms by using CBV

class cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)
    
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('DATA INSERTED SUCCESSFULLY')




