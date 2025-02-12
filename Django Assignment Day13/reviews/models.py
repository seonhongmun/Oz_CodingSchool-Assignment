from django.db import models  # Django의 models 모듈을 임포트
from config.models import BaseModel  # BaseModel 임포트
from users.models import User  # 커스텀 User 모델 임포트
from restaurants.models import Restaurant  # Restaurant 모델 임포트

class Review(BaseModel):
    # BaseModel 상속받아 생성/수정 시간 관리
    user = models.ForeignKey(
        User,  # User 모델 참조
        on_delete=models.CASCADE  # 사용자가 삭제되면 리뷰도 삭제
    )
    restaurant = models.ForeignKey(
        Restaurant,  # Restaurant 모델 참조
        on_delete=models.CASCADE  # 음식점 삭제 시 리뷰도 삭제
    )
    title = models.CharField('리뷰 제목', max_length=50)  # 리뷰 제목 길이 50칸
    comment = models.TextField(verbose_name='리뷰 내용')  # 리뷰 내용

    def __str__(self):
        # 객체 출력 시 제목과 작성자 닉네임 표시
        return f"{self.title} by {self.user.nickname}"
