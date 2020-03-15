from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


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
        return JSONParser(serializer.errors, status=400)
