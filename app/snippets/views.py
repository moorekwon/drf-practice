from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# CRUD(Create Read Update Delete) 구현하기
# 첫 api 구현! localhost:8000/snippets/
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 외부 데이터를 python data type으로 바꿔줌
        data = JSONParser().parse(request)
        # form 쓰는 것처럼 비슷함
        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            # HttpResponse 대신 JsonResponse 사용
            # 따로 renderer 필요하지 않음
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        # 일부만 수정하고 싶을 때, partial=True 사용
        serializer = SnippetSerializer(snippet, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        # 지웠기 때문에 상태코드만 response
        return HttpResponse(status=204)
