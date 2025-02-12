from django.shortcuts import render

from rest_framework import viewsets  # DRF의 viewsets 모듈 임포트
from rest_framework.permissions import AllowAny

from restaurants.models import Restaurant  # Restaurant 모델 임포트
from restaurants.serializers import RestaurantSerializer  # Serializer 임포트

class RestaurantViewset(viewsets.ModelViewSet):
    # ModelViewSet을 상속받아 CRUD 기능을 모두 제공하는 음식점 뷰셋 정의
    queryset = Restaurant.objects.all()  # 조회 대상 쿼리셋 지정
    serializer_class = RestaurantSerializer  # 사용될 Serializer 지정