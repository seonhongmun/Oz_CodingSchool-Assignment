from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:  #이메일 없으면 예외처리
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)  #이메일 정규화(소문자 변환)
        user = self.model(email=email, nickname=nickname, **extra_fields) #사용자
        user.set_password(password)  # 비밀번호 해싱해 저장
        user.save(using=self._db) # 디비에 저장
        return user  # 사용자 반환

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)  # 슈퍼유저 true
        extra_fields.setdefault('is_staff', True)  # 스테프 true
        if extra_fields.get('is_superuser') is not True:  #슈퍼유저가 아니면 예외처리
            raise ValueError('관리자가 아닙니다.')
        return self.create_user(email, nickname, password, **extra_fields)  #사용자 생성메서드 호출

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('이메일', max_length=40, unique=True)  #이메일 필드 하나만존재  길이 40칸
    nickname = models.CharField('닉네임', max_length=20, unique=True)   #닉네임 필드 하나만존재  길이 20칸
    profile_image = models.ImageField(
        '프로필 이미지',
        upload_to='users/profile_images',  # 업로드 경로
        default='users/blank_profile_image.png'  #기본 프로필 이미지 지정
    )
    is_active = models.BooleanField('활성 여부', default=True)  #사용자 활성화여부
    is_staff = models.BooleanField('권한 여부', default=False)   #관리자 권한여보   둘다 기본 없음으로

    objects = CustomUserManager()   #커스텀매니저 지정

    USERNAME_FIELD = 'email'   #로그인시 이메일을 식별자로 사용
    REQUIRED_FIELDS = ['nickname']  # 유저 생성시 닉네임 필수 입력

    def __str__(self):
        return self.email  #객체 반환시 이메일로