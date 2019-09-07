from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	straa= "This text doesn't exist in HTML, it has been passed by views and variables"	
	return render(request, "index.html", {"text" : straa })

def submit(request):
	points= 0
	ans1 = request.GET["HTML"]
	ans2 = request.GET["HTTP"]
	if ans1 == "HTML":
		points = points + 10
	if ans2 == "HTTP": 
		points = points + 10
	return HttpResponse("You managed to score " + str(points) + " points")
