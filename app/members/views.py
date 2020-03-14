from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from config.settings import SECRETS


def login_view(request):
    login_base_url = 'https://nid.naver.com/oauth2.0/authorize'

    login_params = {
        'response_type': 'code',
        'client_id': SECRETS['CLIENT_ID'],
        'redirect_url': 'http://localhost:8000/members/naver-login/',
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

    print('token_url >> ', token_url)
