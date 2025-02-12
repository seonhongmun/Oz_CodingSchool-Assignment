# DRF의 제네릭 뷰를 사용하기 위해 import합니다.
from rest_framework import generics  # DRF의 generics 모듈 import
# 인증된 사용자만 접근할 수 있도록 IsAuthenticated를 import합니다.
from rest_framework.permissions import IsAuthenticated  # 인증 권한 클래스 import
# Response 객체와 HTTP 상태 코드를 사용하기 위해 import합니다.
from rest_framework.response import Response  # Response 객체 import
from rest_framework import status  # HTTP 상태 코드 모듈 import
# get_object_or_404를 사용하여 객체 존재 여부를 확인하기 위해 import합니다.
from django.shortcuts import get_object_or_404  # get_object_or_404 함수 import
# 리뷰 모델을 import합니다.
from reviews.models import Review  # Review 모델 import
# 식당 모델을 import합니다.
from restaurants.models import Restaurant  # Restaurant 모델 import
# 리뷰 관련 시리얼라이저들을 import합니다.
from reviews.serializers import ReviewSerializer, ReviewDetailSerializer  # 시리얼라이저 import

# ReviewListCreateView 정의 (리뷰 리스트 조회 및 생성 APIView)
class ReviewListCreateView(generics.ListCreateAPIView):  # ListCreateAPIView 상속받아 뷰 정의
    serializer_class = ReviewSerializer  # 리뷰 리스트/생성 시 사용할 시리얼라이저 지정
    def get_queryset(self):  # 쿼리셋 반환 메서드 오버라이드
        restaurant_id = self.kwargs.get('restaurant_id')  # URL 파라미터에서 restaurant_id 추출
        # 해당 restaurant_id를 가진 식당의 리뷰만 필터링하여 최신순(내림차순)으로 정렬하여 반환
        return Review.objects.filter(restaurant__id=restaurant_id).order_by('-id')
    def perform_create(self, serializer):  # POST 요청 시 객체 생성 메서드 오버라이드
        restaurant_id = self.kwargs.get('restaurant_id')  # URL 파라미터에서 restaurant_id 추출
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)  # 식당 객체가 존재하는지 확인, 없으면 404 반환
        # 현재 로그인한 사용자와 식당 객체를 사용하여 리뷰 생성 수행
        serializer.save(user=self.request.user, restaurant=restaurant)

# ReviewDetailView 정의 (리뷰 상세 조회, 수정, 삭제 APIView)
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIView 상속받아 뷰 정의
    serializer_class = ReviewDetailSerializer  # 리뷰 상세 시 사용할 시리얼라이저 지정
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능하도록 설정
    def get_object(self):  # 객체 반환 메서드 오버라이드
        review_id = self.kwargs.get('review_id')  # URL 파라미터에서 review_id 추출
        # 요청한 사용자와 일치하는 리뷰를 반환, 없으면 404 에러 반환
        return get_object_or_404(Review, id=review_id, user=self.request.user)
