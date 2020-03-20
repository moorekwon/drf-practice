from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from members.models import User
from members.serializers import UserSerializer


class AuthAPITest(APITestCase):
    # def test_token_api(self):
    #     url = '/members/auth-token/'
    #     username = 'test_username'
    #     password = 'test_passworkd'
    #
    #     # 유저 생성
    #     user = baker.make(User, username=username)
    #     # password는 set_password 함수를 통해 만듦 (해시된 값으로 생성)
    #     # password를 그대로 넣으면 raw string이 들어가게 됨
    #     user.set_password(password)
    #     user.save()
    #
    #     # 전송될 데이터
    #     data = {
    #         'username': username,
    #         'password': password,
    #     }
    #
    #     # post 방식으로 요청 보냄
    #     response = self.client.post(url, data)
    #
    #     # 상태 코드 확인
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # 토큰이 왔는지 확인
    #     self.assertIn('token', response.data)
    #     # 유저 정보가 왔는지 확인
    #     self.assertIn('user', response.data)
    #
    #     # User 인스턴스를 serializer 한 결과가 response.data의 'user' key의 value(object)과 같은지 확인
    #     self.assertEqual(UserSerializer(user).data, response.data['user'])
    #
    #     # 토큰이 있는지 확인
    #     # Token 내장 클래스 > user 필드 > related_name='auth_token'
    #     self.assertIsNotNone(user.auth_token)
    #     # response.data의 'token' key의 value 값이 user와 연결된 Token의 key와 같은지 확인
    #     self.assertEqual(user.auth_token.key, response.data['token'])
    #
    #     print('response.data >> ', response.data)
    #     print('UserSerializer(user).data >> ', UserSerializer(user).data)
    #     print('user.auth_token >> ', user.auth_token)

    def test_login_api(self):
        url = '/members/login/'
        email = 'test@email.com'
        username = 'test'
        password = 'test_password'

        # 유저 생성
        user = baker.make(User, email=email, username=username)
        # password는 set_password 함수를 통해 만듦 (해시된 값으로 생성)
        # password를 그대로 넣으면 raw string이 들어가게 됨
        user.set_password(password)
        user.save()

        # 전송될 데이터
        data = {
            'email': email,
            'username': username,
            'password': password,
        }

        # post 방식으로 요청 보냄
        response = self.client.post(url, data)

        # 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 토큰이 왔는지 확인
        self.assertIn('token', response.data)
        # 유저 정보가 왔는지 확인
        self.assertIn('user', response.data)

        # User 인스턴스를 serializer 한 결과가 response.data의 'user' key의 value(object)과 같은지 확인
        self.assertEqual(UserSerializer(user).data, response.data['user'])

        # 토큰이 있는지 확인
        # Token 내장 클래스 > user 필드 > related_name='auth_token'
        self.assertIsNotNone(user.auth_token)
        # response.data의 'token' key의 value 값이 user와 연결된 Token의 key와 같은지 확인
        self.assertEqual(user.auth_token.key, response.data['token'])

        print('response.data >> ', response.data)
        print('UserSerializer(user).data >> ', UserSerializer(user).data)
        print('user.auth_token >> ', user.auth_token)
