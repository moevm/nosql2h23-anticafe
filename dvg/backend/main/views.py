from django.shortcuts import render
from django.http import JsonResponse
from .models import Order


def post_list(request):
    posts = Post.objects.all()
    data = [{
        "author": p.author.user.username,
        "title": p.title
    } for p in posts]
    return JsonResponse(data, safe=False)
