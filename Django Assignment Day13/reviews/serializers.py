# DRF의 serializers 모듈을 import합니다.
from rest_framework import serializers  # DRF의 serializers 모듈 import
# 리뷰 모델을 import합니다.
from reviews.models import Review  # Review 모델 import (리뷰 앱에 정의되어 있다고 가정)
# 사용자 상세정보를 위한 시리얼라이저를 import합니다.
from users.serializers import UserDetailSerializer  # UserDetailSerializer import
# 식당 정보를 반환하기 위한 RestaurantSerializer를 import합니다.
from restaurants.serializers import RestaurantSerializer  # RestaurantSerializer import (식당 앱에 정의되어 있다고 가정)

# ReviewSerializer 정의 (리뷰 생성 및 리스트 조회용)
class ReviewSerializer(serializers.ModelSerializer):  # ModelSerializer 상속받아 ReviewSerializer 정의
    user = UserDetailSerializer(read_only=True)  # 리뷰 작성자 정보를 UserDetailSerializer로 읽기 전용 설정
    class Meta:  # Meta 클래스 시작
        model = Review  # 시리얼라이저에서 사용할 모델 지정
        fields = ('id', 'user', 'restaurant', 'title', 'comment')  # 사용할 필드 지정
        read_only_fields = ('id', 'restaurant')  # id와 restaurant 필드는 읽기 전용으로 설정

# ReviewDetailSerializer 정의 (리뷰 상세 조회 및 업데이트용)
class ReviewDetailSerializer(serializers.ModelSerializer):  # ModelSerializer 상속받아 ReviewDetailSerializer 정의
    user = UserDetailSerializer(read_only=True)  # 리뷰 작성자 정보를 읽기 전용으로 설정
    restaurant = RestaurantSerializer(read_only=True)  # 식당 정보를 읽기 전용으로 설정
    class Meta:  # Meta 클래스 시작
        model = Review  # 시리얼라이저에서 사용할 모델 지정
        fields = ('id', 'user', 'restaurant', 'title', 'comment')  # 사용할 필드 지정
        read_only_fields = ('id', 'restaurant')  # id와 restaurant 필드는 읽기 전용으로 설정
