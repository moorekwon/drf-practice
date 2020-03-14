import requests
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from config.settings import SECRETS


def login_view(request):
    login_base_url = 'https://nid.naver.com/oauth2.0/authorize'

    login_params = {
        'response_type': 'code',
        'client_id': SECRETS['CLIENT_ID'],
        'redirect_uri': 'http://localhost:8000/members/naver-login/',
        'state': 'RANDOM_STATE',
    }

    login_url = '{base}?{params}'.format(
        base=login_base_url,
        params='&'.join([f'{key}={value}' for key, value in login_params.items()])
    )

    context = {
        'login_url': login_url
    }

    return render(request, 'members/login.html', context)


def naver_login(request):
    code = request.GET.get('code')
    state = request.GET.get('state')

    if (not code) and (not state):
        return HttpResponse('code 또는 state가 전달되지 않았습니다.')

    token_base_url = 'https://nid.naver.com/oauth2.0/token'

    token_params = {
        'grant_type': 'authorization_code',
        'client_id': SECRETS['CLIENT_ID'],
        'client_secret': SECRETS['CLIENT_SECRET'],
        'code': code,
        'state': state,
        'redirectURI': 'http://localhost:8000/members/naver-login/',
    }

    token_url = '{base}?{params}'.format(
        base=token_base_url,
        params='&'.join([f'{key}={value}' for key, value in token_params.items()])
    )

    response = requests.get(token_url)
    print('response.status_code >> ', response.status_code)
    print('response.text >> ', response.text)

    access_token = response.json()['access_token']
    print('access_token >> ', access_token)

    me_url = 'https://openapi.naver.com/v1/nid/me'
    me_headers = {
        'Authorization': f'Bearer {access_token}',
    }
    me_response = requests.get(me_url, headers=me_headers)
    me_response_data = me_response.json()
    print('me_response_data >> ', me_response_data)

    unique_id = me_response_data['response']['id']
    print('unique_id >> ', unique_id)

    # n_{unique_id}의 username을 갖는 새로운 User 생성
    # 생성한 유저를 login 시킴
    naver_username = f'n_{unique_id}'

    if not User.objects.filter(username=naver_username).exists():
        user = User.objects.create_user(username=naver_username)
    else:
        user = User.objects.get(username=naver_username)

    login(request, user)
    return render(request, 'rest_framework/api.html')
