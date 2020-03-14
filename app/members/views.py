from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login_view(request):
    login_base_url = ''

    login_params = {
        'response_type': 'code',
        'client_id': '',
        'redirect_url': '',
        'state': '',
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

    if not code:
        return HttpResponse('code 또는 state가 전달되지 않았습니다.')

    token_base_url = ''

    token_params = {
        'client_id': '',
        'client_secret': '',
        'code': code,
        'state': state,
        'redirectURI': ''
    }

    token_url = '{base}?{params}'.format(
        base=token_base_url,
        params='&'.join([f'{key}={value}' for key, value in token_params.items()])
    )

    print(token_url)
