'''REST_FRAMEWORK의 모듈을 이용하여 GET방식 API를 만드는 코드'''

# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Corpus
from .serializers import CorpusSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hey kkakkung!");