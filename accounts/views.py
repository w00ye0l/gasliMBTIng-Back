from .models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# 회원정보 보기
@api_view(['GET'])
def user_detail(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

# 회원정보 수정
@api_view(['PUT'])
def user_edit(request):
    account_user = User.objects.get(pk=request.user.pk)

    if account_user.username == str(request.user):
        serializer = UserSerializer(account_user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# 회원 탈퇴
@api_view(['DELETE'])
def user_delete(request):
    account_user = User.objects.get(pk=request.user.pk)

    if account_user.username == str(request.user):
        account_user = User.objects.get(pk=request.user.pk)
        account_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
