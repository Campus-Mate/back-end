from django.urls import path
from .views import receive_id, show_id, check_id, delete_id,show_id_by_id,get_all_records
from . import views

urlpatterns = [
    path('receive_id/', receive_id, name='receive_id'),
    path('show_id/', show_id, name='show_id'), # 아이디 값과 제목값 모두 받아서 관련 데이터 출력하는 거
    path('check_id/', check_id, name='check_id'),
    path('delete_id/', delete_id, name='delete_id'),  # 추가된 삭제 엔드포인트
    path('show_id_by_id/',show_id_by_id, name='show_id_by_id'),  # 아이디 값만 받아서 관련 데이터 출력하는거
    path('get_all_records/', get_all_records, name='get_all_records'),  # 새로운 API 경로 추가


    path('', views.index, name='index'),  # 루트 URL에 대한 뷰 정의
]
