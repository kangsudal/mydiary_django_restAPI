'''REST_FRAMEWORK의 모듈을 이용하여 GET방식 API를 만드는 코드'''

# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Corpus
from .serializers import CorpusSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hey kkakkung!");

# [ ]를 입력받았을때 [  ]를 반환해주는 API
@api_view(['GET'])
def randomCorpusAPI(request,id):
    totalCorpuses = Corpus.objects.all()
    randomCorpuses = random.sample(list(totalCorpuses),id) #개수id 만큼 random 생성
    serializer = CorpusSerializer(randomCorpuses, many=True) #many=True는 다량의 데이터도 직렬화가능하게해준다
    return Response(serializer.data)
    # return Response("hey kkakkung!");

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})