'''
 serializer
 - 쿼리셋 및 모델 인스턴스와 같은 복잡한 데이터를 기본 python 데이터 유형으로 변환
 - JSON, XML 및 기타 형식으로 쉽게 렌더링할 수 있음
 - 메모리에 갖고 있는 비연속적인 데이터를 연속적인 데이터(파일, 문자열, )로 만드는 과정

 deserializer
 - 연속적인 데이터를 python이 사용하는 데이터 형태로 만드는 과정

 exclude
 - 특정 필드가 serialize되지 않도록 제외

 ModelSerializer
 - create(), update() 메소드에 대한 기본 구현 존재

 중첩된 직렬화(nested serialization)
 - 기본적으로, 인스턴스는 primary key(기본 키)로 직렬화되어 관계를 나타냄
 - 일반적 방법: depth 파라미터 사용
 - 명시적 방법: 서로 serializer를 정의하고 중첩할 수 있음

 HyperlinkedModelSerializer
 - 브라우저에서 웹 API를 훨씬 더 쉽게 사용 가능, 추가하기 좋은 기능
 - 모든 post가 API의 각 Post 인스턴스에 있는 comment들을 보고 싶다고 가정
    - 중첩된 primary key나 중첩 필드 대신 사용
    - 각 개별 Comment(url)에 대한 링크를 얻음
'''

from rest_framework import serializers

from base.models import Post, Comment


# Post 모델용
class PostSerializer(serializers.ModelSerializer):
    # 하이퍼링크의 또 다른 방법
    # HyperlinkedRelatedField 정의를 일반 serializer에 추가
    # comments = serializers.HyperlinkedRelatedField(many=True, view_name='commnent-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created', 'comments')


# class PostCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'text')

# def save(self):


# HyperlinkedModelSerializer 사용
# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'text', 'created', 'comments')
#         # read_only_fields가 없으면, Post들의 create 양식에는 항상 comments 입력 필요 (의미가 없음)
#         # post에 대한 comments는 일반적으로 post가 작성된 후 만들어짐
#         read_only_fields = ('comments')


# Comment 모델용
class CommentSerializer(serializers.ModelSerializer):
    # 중첩된 직렬화 명시적 방법 사용
    # comment의 post 필드(models.py에서 이름 지정)가 직렬화되지만 PostSerializer에 정의되어 있음
    post = PostSerializer

    class Meta:
        model = Comment
        fields = '__all__'
