# Django의 path 함수를 import합니다.
from django.urls import path  # URL 패턴 생성을 위한 path 함수 import
# 리뷰 관련 뷰들을 import합니다.
from reviews.views import ReviewListCreateView, ReviewDetailView  # 리뷰 뷰 import

# URL 패턴 리스트 정의 시작
urlpatterns = [
    path('restaurants/<int:restaurant_id>/reviews/', ReviewListCreateView.as_view(), name='review-list'),
    # 'restaurants/<int:restaurant_id>/reviews/' 경로에 ReviewListCreateView 연결, 이름: 'review-list'
    path('reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
    # 'reviews/<int:review_id>/' 경로에 ReviewDetailView 연결, 이름: 'review-detail'
]
