# reviews/tests.py
from django.test import TestCase  # Django 테스트 케이스 임포트
from users.models import User  # User 모델 임포트
# DRF의 APITestCase를 import합니다.
from rest_framework.test import APITestCase  # API 테스트 케이스 기본 클래스 import
# URL reverse 함수를 사용하기 위해 import합니다.
from django.urls import reverse  # URL reverse 함수 import
# 현재 활성 사용자 모델을 가져오기 위한 함수를 import합니다.
from django.contrib.auth import get_user_model  # 사용자 모델 가져오기 함수 import
# 레스토랑 모델을 가져옵니다. (식당 앱에 모델이 정의되어 있다고 가정)
from restaurants.models import Restaurant  # Restaurant 모델 import
# 리뷰 모델을 가져옵니다. (리뷰 앱에 모델이 정의되어 있다고 가정)
from reviews.models import Review  # Review 모델 import

# 현재 활성 사용자 모델을 User 변수에 할당합니다.
User = get_user_model()  # 사용자 모델 할당

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

# ReviewAPIViewTestCase 클래스 정의 (리뷰 관련 API 뷰 테스트)
class ReviewAPIViewTestCase(APITestCase):  # APITestCase를 상속받아 테스트 케이스 생성
    def setUp(self):  # 각 테스트 전 초기 설정 메서드
        # 테스트용 사용자를 생성
        self.user = User.objects.create_user(  # 사용자 생성
            email='reviewer@example.com',  # 테스트용 이메일 지정
            password='reviewpassword',  # 테스트용 비밀번호 지정
            nickname='reviewer'  # 테스트용 닉네임 지정
        )
        # 생성한 사용자로 로그인 수행
        self.client.login(  # 세션 로그인 수행
            email='reviewer@example.com',  # 로그인 이메일 지정
            password='reviewpassword'  # 로그인 비밀번호 지정
        )
        # 테스트용 식당을 생성
        self.restaurant = Restaurant.objects.create(  # Restaurant 객체 생성
            name='Test Restaurant'  # 식당 이름 지정
        )
        # 식당 리뷰 리스트 URL을 reverse 함수를 통해 생성 (URL 패턴에 맞춰 kwargs 전달)
        self.review_list_url = reverse('review-list', kwargs={'restaurant_id': self.restaurant.id})

    def test_get_review_list(self):  # 리뷰 리스트 조회 API 뷰 테스트 메서드
        response = self.client.get(self.review_list_url)  # 리뷰 리스트 API에 GET 요청 수행
        self.assertEqual(response.status_code, 200)  # 응답 상태코드가 200 (성공)인지 검증

    def test_post_review(self):  # 리뷰 작성 API 뷰 테스트 메서드
        data = {  # 리뷰 작성에 사용할 데이터 정의
            'title': 'Great Restaurant',  # 리뷰 제목 지정
            'comment': 'Really enjoyed the food!'  # 리뷰 내용 지정
        }
        response = self.client.post(self.review_list_url, data)  # 리뷰 작성 API에 POST 요청 수행
        self.assertEqual(response.status_code, 201)  # 응답 상태코드가 201 (생성)인지 검증

    def test_get_review_detail(self):  # 리뷰 상세 조회 API 뷰 테스트 메서드
        # 테스트용 리뷰를 생성
        review = Review.objects.create(  # Review 객체 생성
            title='Sample Review',  # 리뷰 제목 지정
            comment='Sample comment',  # 리뷰 내용 지정
            user=self.user,  # 리뷰 작성자 지정
            restaurant=self.restaurant  # 리뷰가 속한 식당 지정
        )
        # 리뷰 상세 URL을 reverse 함수를 통해 생성
        review_detail_url = reverse('review-detail', kwargs={'review_id': review.id})
        response = self.client.get(review_detail_url)  # 리뷰 상세 API에 GET 요청 수행
        self.assertEqual(response.status_code, 200)  # 응답 상태코드가 200 (성공)인지 검증

    def test_update_review(self):  # 리뷰 수정 API 뷰 테스트 메서드
        # 테스트용 리뷰를 생성
        review = Review.objects.create(  # Review 객체 생성
            title='Old Title',  # 초기 리뷰 제목 지정
            comment='Old comment',  # 초기 리뷰 내용 지정
            user=self.user,  # 리뷰 작성자 지정
            restaurant=self.restaurant  # 리뷰가 속한 식당 지정
        )
        # 리뷰 상세 URL을 reverse 함수를 통해 생성
        review_detail_url = reverse('review-detail', kwargs={'review_id': review.id})
        data = {  # 리뷰 수정에 사용할 데이터 정의
            'title': 'Updated Title',  # 수정할 리뷰 제목
            'comment': 'Updated comment'  # 수정할 리뷰 내용
        }
        response = self.client.put(review_detail_url, data)  # 리뷰 수정 API에 PUT 요청 수행
        self.assertEqual(response.status_code, 200)  # 응답 상태코드가 200 (성공)인지 검증

    def test_delete_review(self):  # 리뷰 삭제 API 뷰 테스트 메서드
        # 테스트용 리뷰를 생성
        review = Review.objects.create(  # Review 객체 생성
            title='Title to Delete',  # 리뷰 제목 지정
            comment='Comment to delete',  # 리뷰 내용 지정
            user=self.user,  # 리뷰 작성자 지정
            restaurant=self.restaurant  # 리뷰가 속한 식당 지정
        )
        # 리뷰 상세 URL을 reverse 함수를 통해 생성
        review_detail_url = reverse('review-detail', kwargs={'review_id': review.id})
        response = self.client.delete(review_detail_url)  # 리뷰 삭제 API에 DELETE 요청 수행
        self.assertEqual(response.status_code, 204)  # 응답 상태코드가 204 (삭제 성공)인지 검증
