#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myIndex(request):
    my_name = request.POST.get('name' , "CGu")
    return HttpResponse("Hello " + my_name)