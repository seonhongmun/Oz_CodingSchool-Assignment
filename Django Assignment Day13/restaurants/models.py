from django.db import models  # Django의 models 모듈을 임포트합니다.
from config.models import BaseModel  # BaseModel을 임포트합니다.

# 정기 휴무 요일 선택 옵션 정의
DAYS_OF_WEEK = [
    ('MON', 'Monday'),  # 월요일
    ('TUE', 'Tuesday'),  # 화요일
    ('WED', 'Wednesday'),  # 수요일
    ('THU', 'Thursday'),  # 목요일
    ('FRI', 'Friday'),  # 금요일
    ('SAT', 'Saturday'),  # 토요일
    ('SUN', 'Sunday'),  # 일요일
]

class Restaurant(BaseModel):
    # BaseModel을 상속받아 생성/수정 시간 자동 관리
    name = models.CharField('음식점 이름', max_length=50)  # 음식점 이름 길이 50칸
    address = models.CharField('음식점 주소', max_length=200)  # 음식점 주소 길이 200칸
    contact = models.CharField('연락처 정보', max_length=50)  # 연락처 정보 길이 50칸
    open_time = models.TimeField('영업 시작 시간 ', null=True, blank=True)  # 영업 시작 시간
    close_time = models.TimeField('영업 종료 시간 ' , null=True, blank=True)  # 영업 종료 시간
    last_order = models.TimeField('마지막 주문 시간 ', null=True, blank=True)  # 마지막 주문 시간
    regular_holiday = models.CharField(
        max_length=3,  # 'MON' 등 3글자로 지정
        choices=DAYS_OF_WEEK,  # 선택 옵션 지정
        null=True,  # null 허용
        blank=True  # 빈 값 허용
    )

    def __str__(self):
        return self.name  # 객체 출력 시 음식점 이름 반환

