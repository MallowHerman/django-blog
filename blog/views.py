from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'Herman Gonçalves',
        'title': 'Blog Post 1',
        'content': 'blablabla',
        'date_posted': '23/11/2022'
    },
    {
        'author': 'Herman Gonçalves',
        'title': 'Blog Post 1',
        'content': 'blablabla',
        'date_posted': '23/11/2022'
    },
    {
        'author': 'Herman Gonçalves',
        'title': 'Blog Post 1',
        'content': 'blablabla',
        'date_posted': '23/11/2022'
    }
]

def home(request):
	return render(request, 'blog/home.html', {'posts':posts, 'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html')