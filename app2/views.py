from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2_string(request):
    return HttpResponse('THIS IS MY BEAUTIFUL FUNCTION')
def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')
