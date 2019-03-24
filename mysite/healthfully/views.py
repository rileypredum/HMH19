from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from pymongo import MongoClient

client = MongoClient(port=27017)

def showContent():
	print("hiii");
	return render(request, 'index.html', context={'showContentBool': 'true'})

def index(request):
	return render(request, 'index.html', context={'showContentBool': 'false'})
    # return HttpResponse("Hello, world.")