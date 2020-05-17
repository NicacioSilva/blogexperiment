from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nicacio',
        'title': 'Frist Post',
        'content': 'First post content',
        'date_posted': 'May 16, 2020'
    },
    {
        'author': 'Rebeca',
        'title': 'Second Post',
        'content': 'Second post content',
        'date_posted': 'May 17, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
