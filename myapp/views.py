# backend/myapp/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

stored_id = None  # 전역 변수로 ID 값 저장

@csrf_exempt
def receive_id(request):
    if request.method == 'POST':
        global stored_id
        data = json.loads(request.body)
        stored_id = data.get('id')
        return JsonResponse({'message': 'ID received successfully'})
        

def show_id(request):
    return render(request, 'show_id.html', {'id': stored_id})
