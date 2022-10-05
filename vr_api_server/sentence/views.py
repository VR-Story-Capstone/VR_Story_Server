from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from venv import create
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sentence
from .serializers import SentenceSerializer 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    

class SentenceView(APIView):
    """
    GET all sentences
    request parameters: None

    """
    def get(self, request):
        # 모든 문장 리스트 불러옴
        sentence_queryset = Sentence.objects.all() 
        sentence_queryset_serializer = SentenceSerializer(sentence_queryset, many = True)
        return Response(sentence_queryset_serializer.data, status=status.HTTP_200_OK)

    """
    POST
    request parameters:: {
        "sentence_type" : Integer
        "subject" : String,
        "complement" : String,
        "object" : String,
        "modifier" : String,
        "predicate" : String
    }
    """
    def post(self, request):
        data = request.data
        sentence_serializer = SentenceSerializer(data = request.data)
        
        # 유효성 검사 
        if sentence_serializer.is_valid():
            # DB에 저장
            sentence_serializer.save()
            # 성공적으로 DB에 저장 시 해당 
            user_id = sentence_serializer.data.get("user_id")
            sentence_queryset = Sentence.objects.filter().order_by('-id')[0]
            sentence_serializer = SentenceSerializer(sentence_queryset)
            return Response(sentence_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sentence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)