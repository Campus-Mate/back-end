from django.http import HttpResponse
from django.shortcuts import render

import os

# def serve_react_app(request):
    # """
    # 뷰 함수에서 리액트 앱의 index.html 파일을 직접 제공합니다.
    # """
    # filepath = os.path.join(os.path.dirname(__file__), 'static', 'react_app', 'index.html')
    # with open(filepath, 'r') as file:
    #     return HttpResponse(file.read(), content_type='text/html')
def serve_react_app(request):
    return render(request, 'index.html')
