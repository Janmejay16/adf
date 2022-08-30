from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def custom(request):
    return render(request, 'home.html',{
        "name":"Janmejay",
        "arr": ['C++', 'JavaScript', 'Python']
    })