from rest_framework import serializers  # DRF의 serializers 모듈 임포트
from restaurants.models import Restaurant  # Restaurant 모델 임포트

class RestaurantSerializer(serializers.ModelSerializer):
    # Restaurant 모델의 데이터를 직렬화/역직렬화하기 위한 Serializer

    class Meta:
        model = Restaurant  # 대상 모델 지정
        fields = '__all__'  # 모든 필드를 포함 (읽기/쓰기 모두 가능)
