# reviews/tests.py
from django.test import TestCase  # Django 테스트 케이스 임포트
from users.models import User  # User 모델 임포트
from restaurants.models import Restaurant  # Restaurant 모델 임포트
from reviews.models import Review  # Review 모델 임포트

class ReviewModelTest(TestCase):
    # Review 모델 관련 테스트 케이스 정의

    def setUp(self):
        # 테스트 전 기본 데이터 설정
        self.user = User.objects.create_user(
            email='reviewer@example.com',  # 리뷰어 이메일
            nickname='reviewer',  # 리뷰어 닉네임
            password='password123'  # 리뷰어 비밀번호
        )
        self.restaurant = Restaurant.objects.create(
            name='아웃백',  # 음식점 이름
            address='서울 구로구',  # 음식점 주소
            contact='010-1234-5678',  # 연락처
            open_time='10:00',  # 영업 시작 시간
            close_time='23:00',  # 영업 종료 시간
            last_order='22:30',  # 마지막 주문 시간
            regular_holiday='MON'  # 정기 휴무 요일
        )
        self.review_data = {
            'title': '맛있다',  # 리뷰 제목
            'comment': '스테이크 짱'  # 리뷰 내용
        }

    def test_create_review(self):
        # Review 객체 생성 테스트
        review = Review.objects.create(
            user=self.user,  # 리뷰어 연결
            restaurant=self.restaurant,  # 음식점 연결
            title=self.review_data['title'],  # 제목 전달
            comment=self.review_data['comment']  # 내용 전달
        )
        self.assertEqual(review.title, self.review_data['title'])  # 제목 확인
        self.assertEqual(review.comment, self.review_data['comment'])  # 내용 확인
        self.assertEqual(review.user, self.user)  # 연결된 사용자 확인
        self.assertEqual(review.restaurant, self.restaurant)  # 연결된 음식점 확인
