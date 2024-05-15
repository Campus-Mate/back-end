from django.shortcuts import render

def serve_react_app(request):
    """
    뷰 함수에서 리액트 앱의 index.html 파일을 제공합니다.
    """
    return render(request, 'react_app/index.html')
