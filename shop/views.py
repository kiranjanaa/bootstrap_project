from django.shortcuts import render

# Create your views here.
def movies(request):
    return render(request,'movies.html')
def movies1(request):
    return render(request,'movies1.html')
def allmovies(request):
    return render(request,'allmovies.html')