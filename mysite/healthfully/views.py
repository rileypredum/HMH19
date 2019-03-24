from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from pymongo import MongoClient

client = MongoClient(port=27017)

def index(request):
	return render(request, 'index.html', context={
		"blogs": [1,2,3, 4, 5, 6],
		"communities": [1,2,3],
	})
    # return HttpResponse("Hello, world.")