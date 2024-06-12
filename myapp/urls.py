from django.urls import path
from .views import receive_id, show_id, check_id, delete_id
from . import views

urlpatterns = [
    path('receive_id/', receive_id, name='receive_id'),
    path('show_id/', show_id, name='show_id'),
    path('check_id/', check_id, name='check_id'),
    path('delete_id/', delete_id, name='delete_id'),  # 추가된 삭제 엔드포인트
    
    path('', views.index, name='index'),  # 루트 URL에 대한 뷰 정의
]
