'''
(일반적으로) generic class-based 뷰 및 viewsets를 사용
- 자동으로 수행할 수 있음
- settings.py에 추가하기만 하면 됨

APIView를 사용
- 명시적으로 적용해야 함
- settings.py에 설정 추가 후 작성
- 뷰(APIView)를 통해 pagination 처리
'''

from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.views import APIView


class PostView(APIView):
    # 쿼리셋, serializer_class, 등등
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    # pagination을 달성하려면 get 메소드를 재정의 해야함
    def get(self, request):
        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = self.serializer_class(page, mamy=True)
            return self.get_paginated_response(serializer.data)

    # pagination 핸들러(django-rest-framework/rest_framework/generics.py) 추가
    @property
    # 뷰와 관련된 paginator 인스턴스 또는 없음(None)
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    # 한 페이지의 결과를 반환하거나, pagination이 비활성화된 경우 None 반환
    def paginate_queryset(self, queryset):
        if self.paginator is not None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    # 주어진 출력 데이터에 대해 paginate된 스타일의 Response 객체를 반환
    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)


# 자체 paginatino 클래스를 정의하고 기본 속성을 재정의
# LimitOffsetPagination 또는 DRF에서 제공하는 다른 뷰 대신, 하나/여러/모든 뷰에서 이 뷰를 사용하도록 함
# 클라이언트는 (쿼리 매개변수(query param) 포함) 응답 페이지 크기를 최대 max_page_size, 기본값 page_size로 제한
class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000
