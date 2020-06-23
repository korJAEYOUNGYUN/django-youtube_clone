from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# TODO: 비디오 리스트, 한개보내기, 회원가입,
# TODO: 인증: 로그인, 로그아웃, 비디오 수정, 비디오 삭제, 프로필 수정, 유저 상세정보, 비밀번호 변경


# class VideoViewSet:


class UserLoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        })