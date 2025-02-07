from django.test import TestCase

from restaurants.models import Restaurant


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
