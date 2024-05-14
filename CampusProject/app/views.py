from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def home(request):
    return HttpResponse("Welcome to the Campus Project!")

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'app/post_list.html', {'posts': posts})