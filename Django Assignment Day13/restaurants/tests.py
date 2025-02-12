from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APITestCase
from restaurants.models import Restaurant
# restaurants/test.py
from rest_framework.test import APITestCase  # DRF의 API 테스트 케이스 임포트
from django.urls import reverse  # URL 역참조를 위한 reverse 임포트
from restaurants.models import Restaurant  # Restaurant 모델 임포트

User = get_user_model()

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant_data = {
            'name': '쭉심',  # 음식점 이름
            'address': '서울 오류동',  # 음식점 주소
            'contact': '010-1234-5678',  # 연락처
            'open_time': '09:00',  # 영업 시작 시간
            'close_time': '22:00',  # 영업 종료 시간
            'last_order': '21:30',  # 마지막 주문 시간
            'regular_holiday': 'SUN'  # 정기 휴무 요일
        }

    def test_create_restaurant(self):
        # Restaurant 객체 생성 테스트
        restaurant = Restaurant.objects.create(
            name=self.restaurant_data['name'],  # 이름 전달
            address=self.restaurant_data['address'],  # 주소 전달
            contact=self.restaurant_data['contact'],  # 연락처 전달
            open_time=self.restaurant_data['open_time'],  # 영업 시작 시간 전달
            close_time=self.restaurant_data['close_time'],  # 영업 종료 시간 전달
            last_order=self.restaurant_data['last_order'],  # 마지막 주문 시간 전달
            regular_holiday=self.restaurant_data['regular_holiday']  # 정기 휴무 요일 전달
        )
        self.assertEqual(restaurant.name, self.restaurant_data['name'])  # 이름 확인
        self.assertEqual(restaurant.address, self.restaurant_data['address'])  # 주소 확인
        self.assertEqual(restaurant.contact, self.restaurant_data['contact'])  # 연락처 확인
        self.assertEqual(restaurant.regular_holiday, self.restaurant_data['regular_holiday'])  # 정기 휴무 요일 확인


class RestaurantViewTestCase(APITestCase):
    # Restaurant 뷰셋 관련 테스트 케이스 정의

    def setUp(self):
        self.user = User.objects.create_user(
            email = 'test@test.com',
            password = 'password123',
            nickname = 'testname'
        )
        self.client.login(
            email='test@test.com',
            password='password123'
        )

        # 테스트 전 기본 데이터 생성
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',  # 음식점 이름
            address='789 Test Blvd',  # 음식점 주소
            contact='010-1111-2222',  # 연락처
            open_time='08:00',  # 영업 시작 시간
            close_time='20:00',  # 영업 종료 시간
            last_order='19:30',  # 마지막 주문 시간
            regular_holiday='SAT'  # 정기 휴무 요일
        )
        self.list_url = reverse('restaurant-list')  # 리스트 엔드포인트 URL 역참조
        self.detail_url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.pk})  # 상세 엔드포인트 URL 생성

    def test_restaurant_list_view(self):
        # GET 요청을 통한 음식점 목록 조회 테스트
        response = self.client.get(self.list_url)  # 리스트 URL에 GET 요청
        self.assertEqual(response.status_code, 200)  # 상태 코드 200 확인

    def test_restaurant_post_view(self):
        # POST 요청을 통한 음식점 생성 테스트
        data = {
            'name': '토라',  # 새 음식점 이름
            'address': '서울 오류동 1',  # 새 음식점 주소
            'contact': '010-1111-2222',  # 새 연락처
            'open_time': '10:00',  # 새 영업 시작 시간
            'close_time': '22:00',  # 새 영업 종료 시간
            'last_order': '21:30',  # 새 마지막 주문 시간
            'regular_holiday': 'SUN'  # 새 정기 휴무 요일
        }
        response = self.client.post(self.list_url, data, format='json')  # POST 요청, JSON 포맷 지정
        self.assertEqual(response.status_code, 201)  # 생성 성공시 201 상태 코드 확인
        self.assertEqual(Restaurant.objects.count(), 2)  # 음식점 객체 총 개수가 2개인지 확인

    def test_restaurant_detail_view(self):
        # GET 요청을 통한 음식점 상세 조회 테스트
        response = self.client.get(self.detail_url)  # 상세 URL에 GET 요청
        self.assertEqual(response.status_code, 200)  # 상태 코드 200 확인
        self.assertEqual(response.data['name'], self.restaurant.name)  # 응답 데이터의 이름이 일치하는지 확인

    def test_restaurant_update_view(self):
        # PATCH 요청을 통한 음식점 정보 업데이트 테스트
        data = {
            'name': 'Updated Restaurant',  # 변경될 음식점 이름
            'address': self.restaurant.address,  # 기존 주소 유지
            'contact': self.restaurant.contact,  # 기존 연락처 유지
            'open_time': self.restaurant.open_time,  # 기존 영업 시작 시간 유지
            'close_time': self.restaurant.close_time,  # 기존 영업 종료 시간 유지
            'last_order': self.restaurant.last_order,  # 기존 마지막 주문 시간 유지
            'regular_holiday': self.restaurant.regular_holiday  # 기존 정기 휴무 요일 유지
        }
        response = self.client.patch(self.detail_url, data, format='json')  # PATCH 요청, JSON 포맷 지정
        self.assertEqual(response.status_code, 200)  # 상태 코드 200 확인
        self.restaurant.refresh_from_db()  # DB에서 최신 데이터로 갱신
        self.assertEqual(self.restaurant.name, 'Updated Restaurant')  # 업데이트 결과 확인

    def test_restaurant_delete_view(self):
        # DELETE 요청을 통한 음식점 삭제 테스트
        response = self.client.delete(self.detail_url)  # 상세 URL에 DELETE 요청
        self.assertEqual(response.status_code, 204)  # 상태 코드 204 (No Content) 확인
        self.assertEqual(Restaurant.objects.count(), 0)  # 음식점 객체가 삭제되었는지 확인
