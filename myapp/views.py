# backend/myapp/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IDRecord
from .serializers import IDRecordSerializer
import json

@csrf_exempt
@api_view(['POST'])  # RESTful API POST 요청을 처리
def receive_id(request):
    if request.method == 'POST':
        serializer = IDRecordSerializer(data=request.data)
        if serializer.is_valid():  # 데이터가 유효한지 검사
            serializer.save()  # 데이터베이스에 저장
            print("Data saved:", serializer.data)  # 데이터 저장 로그 출력
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)  # 유효성 검사 오류 로그 출력
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
def show_id(request):
    try:
        latest_record = IDRecord.objects.latest('created_at')  # 가장 최근에 생성된 레코드를 조회
        return render(request, 'show_id.html', {
            'id': latest_record.id_value,
            'content': latest_record.content,
            'category': latest_record.category,
            'created_at': latest_record.created_at
        })
    except IDRecord.DoesNotExist:
        return render(request, 'show_id.html', {
            'error': 'No records found'
        })
@csrf_exempt
@api_view(['POST'])
def check_id(request):
    # 클라이언트로부터 받은 ID 토큰
    id_token = request.data.get('id_value')
    
    # 데이터베이스에서 ID 토큰과 일치하는 레코드를 찾습니다.
    try:
        record = IDRecord.objects.get(id_value=id_token)
        serializer = IDRecordSerializer(record)
        return JsonResponse(serializer.data, status=200)
    except IDRecord.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

#2
# #backend/myapp/views.py
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json
# stored_id = None  # 전역 변수로 ID 값 저장
# stored_content = None  # 전역 변수로 ID 값 저장
# stored_date = None  # 전역 변수로 ID 값 저장
# stored_category = None  # 전역 변수로 ID 값 저장
# @csrf_exempt
# def receive_id(request):
#     if request.method == 'POST':
#         global stored_id,stored_content,stored_date,stored_category
#         data = json.loads(request.body)

#         stored_id = data.get('id')
#         stored_content = data.get('content')
#         stored_date = data.get('date')
#         stored_category = data.get('category')
#         return JsonResponse({'message': 'ID received successfully'})
        

# def show_id(request):
#     return render(request, 'show_id.html', {
#         'id': stored_id,
#         'content': stored_content,
#         'date': stored_date,
#         'category': stored_category
#         })

#1
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
