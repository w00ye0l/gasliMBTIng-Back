from django.shortcuts import render
from .models import Guestbook
from .serializers import GuestbookSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 방명록 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def guestbook_list(request):
    guestbooks = Guestbook.objects.all()
    serializer = GuestbookSerializer(guestbooks, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def guestbook_filter(request):
#     print(request.data)
#     guestbooks = Guestbook.objects.filter(group=request.data['filter'])
#     serializer = GuestbookSerializer(guestbooks, many=True)
#     return Response(serializer.data)

# 방명록 글 생성 
@api_view(['POST'])
@permission_classes([AllowAny])
def guestbook_create(request):
    print(request.user)
    print(request.data)
    serializer = GuestbookSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        guestbook = Guestbook.objects.order_by('-pk')[0]
        print(guestbook)
        return_serializer = GuestbookSerializer(guestbook)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)

# 방명록 상세 내용 확인 
@api_view(['GET'])
@permission_classes([AllowAny])
def guestbook_detail(request, pk):
    try:
        guestbook = Guestbook.objects.get(pk=pk)
    except Guestbook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GuestbookSerializer(guestbook)
    return Response(serializer.data)
    
# 방명록 수정
# @api_view(['PUT'])
# @permission_classes([AllowAny])
# def guestbook_update(request, pk):
#     guestbook = Guestbook.objects.get(pk=pk)
#     serializer = GuestbookSerializer(guestbook, request.data)
# 
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 방명록 삭제 - 로그인 필요
@api_view(['DELETE'])
def guestbook_delete(request, pk):
    guestbook = Guestbook.objects.get(pk=pk)
    guestbook.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 