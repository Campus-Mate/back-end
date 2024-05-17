from django.urls import path
from .views import KakaoLoginView, KakaoCallbackView, PostListView, PostCreateView

urlpatterns = [
    path('kakao-login/', KakaoLoginView.as_view(), name='kakao-login'),
    path('auth/kakao/callback/', KakaoCallbackView.as_view(), name='kakao-callback'),  # 카카오 콜백 URL 추가
    path('posts/<int:user_id>/', PostListView.as_view(), name='post-list'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
]
