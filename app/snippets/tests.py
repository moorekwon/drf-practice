import random

from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

# Postman이 하는 일을 코드로 자동화하여 테스트
# DB는 분리됨
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetTest(APITestCase):
    def test_snippet_list(self):
        url = '/snippets/'

        for i in range(5):
            Snippet.objects.create(code='1')

        # self.client => requests와 같은 역할
        response = self.client.get(url)

        # response.data는 python data type 형으로 나옴
        # print('response.data >> ', response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        for snippet_data in response.data:
            self.assertIn('title', snippet_data)
            self.assertIn('code', snippet_data)
            self.assertIn('linenos', snippet_data)
            self.assertIn('language', snippet_data)
            self.assertIn('style', snippet_data)
            self.assertEqual('1', snippet_data['code'])

            pk = snippet_data['pk']
            # print('pk >> ', pk)
            snippet = Snippet.objects.get(pk=pk)
            # print('snippet >> ', snippet)
            # print('SnippetSerializer(snippet).data >> ', SnippetSerializer(snippet).data)
            # print('snippet_data >> ', snippet_data)
            self.assertEqual(SnippetSerializer(snippet).data, snippet_data)

    def test_snippet_create(self):
        url = '/snippets/'

        data = {
            'code': 'def abc():',
        }

        response = self.client.post(url, data=data)
        # print('response.data >> ', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data['pk']
        snippet = Snippet.objects.get(pk=pk)
        # print('pk >> ', pk)
        # print('snippet, snippet.pk >> ', snippet, snippet.pk)
        # print('SnippetSerializer(snippet).data >> ', SnippetSerializer(snippet).data)
        self.assertEqual(SnippetSerializer(snippet).data, response.data)
        self.assertEqual(Snippet.objects.count(), 1)

    def test_snippet_delete(self):
        # 객체 5개 생성
        snippets = [Snippet.objects.create(code='3') for i in range(5)]
        print('snippets5 >> ', snippets)
        # 객체가 5개인지 확인
        self.assertEqual(Snippet.objects.count(), 5)

        # 아무거나 1개 선택
        snippet = random.choice(snippets)
        print('snippet, snippet.pk >> ', snippet, snippet.pk)

        url = f'/snippets/{snippet.pk}/'
        # delete API 실행
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # 객체가 4개가 되었는지 확인
        self.assertEqual(Snippet.objects.count(), 4)
        print('Snippet.objects.all() >> ', Snippet.objects.all())
        self.assertFalse(Snippet.objects.filter(pk=snippet.pk).exists())