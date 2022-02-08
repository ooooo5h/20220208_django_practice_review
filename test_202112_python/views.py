from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_home(request):
    
    content = '<h1>까꿍!</h1>'
    
    return HttpResponse(content)