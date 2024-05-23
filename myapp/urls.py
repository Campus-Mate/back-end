# backend/myapp/urls.py
from django.urls import path
from .views import receive_id, show_id, check_id

urlpatterns = [
    path('receive_id/', receive_id, name='receive_id'),
    path('show_id/', show_id, name='show_id'),
    path('check_id/', check_id, name='check_id'),

]

