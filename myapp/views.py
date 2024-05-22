#backend/myapp/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
stored_id = None  # 전역 변수로 ID 값 저장
stored_content = None  # 전역 변수로 ID 값 저장
stored_date = None  # 전역 변수로 ID 값 저장
stored_category = None  # 전역 변수로 ID 값 저장
@csrf_exempt
def receive_id(request):
    if request.method == 'POST':
        global stored_id,stored_content,stored_date,stored_category
        data = json.loads(request.body)

        stored_id = data.get('id')
        stored_content = data.get('content')
        stored_date = data.get('date')
        stored_category = data.get('category')
        return JsonResponse({'message': 'ID received successfully'})
        

def show_id(request):
    return render(request, 'show_id.html', {
        'id': stored_id,
        'content': stored_content,
        'date': stored_date,
        'category': stored_category
        })

# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import IDRecord
# from .serializers import IDRecordSerializer

# # ID 값을 저장할 전역 변수
# stored_id = None

# @api_view(['POST'])
# def receive_id(request):
#     global stored_id
#     if request.method == 'POST':
#         serializer = IDRecordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             stored_id = serializer.data.get('id_value')  # 저장된 ID를 전역 변수에 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def show_id(request):
#     return render(request, 'show_id.html', {'id': stored_id})
