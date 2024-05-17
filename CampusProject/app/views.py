from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Post
from .serializers import UserSerializer, PostSerializer
from django.conf import settings
import os
import requests

def serve_react_app(request):
    return render(request, 'index.html')

class KakaoLoginView(APIView):
    def post(self, request):
        kakao_id = request.data.get('kakao_id')
        username = request.data.get('username')
        email = request.data.get('email')

        if not kakao_id:
            return Response({"error": "Kakao ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = CustomUser.objects.get_or_create(kakao_id=kakao_id, defaults={'username': username, 'email': email})

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class KakaoCallbackView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        token_url = 'https://kauth.kakao.com/oauth/token'
        token_data = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_REST_API_KEY,
            'redirect_uri': settings.KAKAO_REDIRECT_URI,
            'code': code,
        }
        token_headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        token_response = requests.post(token_url, data=token_data, headers=token_headers)
        token_json = token_response.json()
        access_token = token_json.get('access_token')

        user_info_url = 'https://kapi.kakao.com/v2/user/me'
        user_info_headers = {
            'Authorization': f'Bearer {access_token}',
        }
        user_info_response = requests.get(user_info_url, headers=user_info_headers)
        user_info_json = user_info_response.json()

        kakao_id = user_info_json['id']
        email = user_info_json['kakao_account']['email']
        nickname = user_info_json['properties']['nickname']

        user, created = CustomUser.objects.get_or_create(kakao_id=kakao_id, defaults={'username': nickname, 'email': email})

        # 로그인 후 홈 페이지로 리디렉션
        return redirect('home')

class PostListView(APIView):
    def get(self, request, user_id):
        posts = Post.objects.filter(author=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostCreateView(APIView):
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        user_id = request.data.get('user_id')

        author = CustomUser.objects.get(id=user_id)
        post = Post(title=title, content=content, author=author)
        post.save()

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
