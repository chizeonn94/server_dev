from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import LoginUser


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg='해당 사용자가 없습니다.', ))
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg='로그인 성공', user_id=user.user_id, birth_day=user.birth_day,
                                 gender=user.gender, email=user.email, name=user.name, age=user.age))
        else:
            return Response(dict(msg='로그인 실패'))


class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        birth_day = request.data.get('birth_day')
        gender = request.data.get('gender')
        email = request.data.get('email')
        name = request.data.get('name')
        age = request.data.get('age')

        user_pw_encrypted = make_password(user_pw)
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is not None:
            return Response(dict(msg="동일한 아이디가 있습니다."))
        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encrypted,
                                 birth_day=birth_day, gender=gender, email=email, name=name, age=age)
        data = dict(
            user_id=user_id,
            user_pw=user_pw_encrypted,
            birth_day=birth_day,
            gender=gender,
            email=email,
            name=name,
            age=age
        )
        # print('>>>>.', request.data)

        return Response(data)

    def get(self, request):
        print(request)
        return request
