from django.http import JsonResponse
from django.shortcuts import render

def hello_json(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_html(request):
    return render(request, 'helloapp/hello.html')
