from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	straa= "This text doesn't exist in HTML, it has been passed by views and variables"	
	return render(request, "index.html", {"text" : straa })

def submit(request):
	name = request.GET["username"]
	return HttpResponse(name)