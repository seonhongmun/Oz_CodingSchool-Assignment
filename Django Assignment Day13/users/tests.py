from django.contrib.auth import get_user_model
from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.test import APITestCase
from users.models import User

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email':'test@test.com',
            'nickname':'test',
            'password':'password123'
        }

    def test_user_manager_create_user(self):
        user = User.objects.create_user(
            email=self.user_data['email'],
            nickname=self.user_data['nickname'],
            password=self.user_data['password']
        )
        self.assertEqual(user.email, self.user_data['email'])  # 이메일이 동일한지 확인
        self.assertEqual(user.nickname, self.user_data['nickname'])  # 닉네임이 동일한지 확인
        self.assertNotEqual(user.password, self.user_data['password'])  # 비밀번호가 해싱되어 저장되었는지 확인
        self.assertTrue(user.is_active)  # 기본 활성화 상태 확인

    def test_user_manager_superuser(self):
        admin_user = User.objects.create_superuser(
            email='admin_test@test.com',
            nickname='admintest',
            password='admin123'
            )
        self.assertEqual(admin_user.email, 'admin_test@test.com')  # 이메일 확인
        self.assertEqual(admin_user.nickname, 'admintest')  # 닉네임 확인
        self.assertTrue(admin_user.is_superuser)  # 슈퍼유저 플래그 확인
        self.assertTrue(admin_user.is_staff)  # 관리자 접근 권한 확인

class UserAPIViewTestCase(APITestCase):
    permission_classes = [AllowAny]

    def setUp(self):
        from django.urls import reverse
        self.signup_url = reverse('user-signup')
        self.login_url = reverse('user-login')
        self.detail_url = lambda pk: reverse('user-detail', kwargs={'pk': pk})

    def test_user_signup(self):
        data = {
            'nickname':'newuser',
            'email':'newuser@example.com',
            'password':'newpassword123'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        user = User.objects.create_user(
            email = 'testlogin@example.com',
            password = 'testpassword123',
            nickname = 'testlogin'
        )
        data = {
            'email':'testlogin@example.com',
            'password':'testpassword123'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_login_invalid_credentials(self):
        data = {
            'email':'testlogin@example.com',
            'password':'invalidpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 400)

    def test_get_user_details(self):
        user = User.objects.create_user(
            email='detail@example.com',
            password='detailpassword123',
            nickname='detailuser'
        )
        self.client.login(
            email='detail@example.com',
            password='detailpassword123'
        )
        response = self.client.get(self.detail_url(user.pk))
        self.assertEqual(response.status_code, 200)

    def test_update_user_datails(self):
        user = User.objects.create_user(
            email='update@example.com',
            password='updatepassword123',
            nickname='updateuser'
        )
        self.client.login(
            email='update@example.com',
            password='updatepassword123'
        )
        data = {
            'nickname':'updateduser',
            'email':'updateduser@example.com',
            'password':'updatedpassword123'
        }
        response = self.client.put(self.detail_url(user.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user = User.objects.create_user(
            email='delete@example.com',
            password='deletepassword123',
            nickname='deleteuser'
        )
        self.client.login(
            email='delete@example.com',
            password='deletepassword123'
        )
        response = self.client.delete(self.detail_url(user.pk))
        self.assertEqual(response.status_code, 204)