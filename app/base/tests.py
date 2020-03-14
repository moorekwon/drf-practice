'''
API가 작동하는지 테스트

APIRequestFactory
- Django의 RequestFactory 클래스와 이름이 비슷
- 다른 클래스 메소드를 사용해 API에 테스트 요청을 보낼 수 있음

'''
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory

from base.models import Post
from base.views import PostList


# Post 모델에 대한 테스트 요청 작성
# PostList 뷰(class-based 뷰)로 테스트
class PostTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.post = Post.objects.create(title='Post example', text='Lorem Ipsum')

    # HTTP 메소드 GET
    def get(self):
        view = PostList.as_view()
        request = self.factory.get('/posts/')
        response = view(request)

        # 200 = OK
        self.assertEqual(response.status_code, 200)

    # HTTP 메소드 POST
    def post(self):
        view = PostList.as_view()

        # request 생성
        request = self.factory.post('/posts/', {
            'title': 'Post example',
            'text': 'Lorem Ipsum'
        })

        response = view(request)
        expected = {'title': self.post.title, 'text': self.post.text}

        # 201 = created
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected)
