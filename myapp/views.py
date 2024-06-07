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
    id_token = request.data.get('id_value')
    if not id_token:
        return JsonResponse({'error': 'ID value is required'}, status=400)
    try:
        records = IDRecord.objects.filter(id_value=id_token)
        if records.exists():
            serializer = IDRecordSerializer(records, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)
        else:
            return JsonResponse({'error': 'Record not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Internal Server Error'}, status=500)

@csrf_exempt
@api_view(['POST'])
def check_id(request):
    # 클라이언트로부터 받은 ID 토큰
    id_token = request.data.get('id_value')
    
    # 유효한 요청인지 확인합니다.
    if not id_token:
        return JsonResponse({'error': 'ID value is required'}, status=400)
    try:
        # 데이터베이스에서 ID 토큰과 일치하는 레코드를 찾습니다.
        record = IDRecord.objects.get(id_value=id_token)
        serializer = IDRecordSerializer(record)
        return JsonResponse(serializer.data, status=200)
    except IDRecord.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)
    except Exception as e:
        # 알 수 없는 예외가 발생한 경우 로그를 출력하고 500 에러를 반환합니다.
        print(f"Unexpected error occurred: {e}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
def index(request):
    return render(request, 'index.html')