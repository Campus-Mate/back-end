# backend/myapp/urls.py
from django.urls import path
from .views import receive_id, show_id, check_id
from .import views

urlpatterns = [
    path('receive_id/', receive_id, name='receive_id'),
    path('show_id/', show_id, name='show_id'),
    path('check_id/', check_id, name='check_id'),
    path('', views.index, name='index'),  # 루트 URL에 대한 뷰 정의

]

