from django.test import TestCase

from users.models import User


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