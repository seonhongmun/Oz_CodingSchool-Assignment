from django.db import models

class Todo(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="제목"  # 필드 라벨을 "제목"으로 설정
    )
    description = models.TextField(
        verbose_name="내용"  # 필드 라벨을 "내용"으로 설정
    )
    start_date = models.DateField(
        verbose_name="시작 날짜"  # 필드 라벨을 "시작 날짜"로 설정
    )
    end_date = models.DateField(
        verbose_name="종료 날짜"  # 필드 라벨을 "종료 날짜"로 설정
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="완료 여부"  # 필드 라벨을 "완료 여부"로 설정
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성 날짜"  # 필드 라벨을 "생성 날짜"로 설정
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="수정 날짜"  # 필드 라벨을 "수정 날짜"로 설정
    )

    class Meta:
        verbose_name = "할 일"  # 모델 이름(단수형)을 "할 일"로 설정
        verbose_name_plural = "할 일 목록"  # 모델 이름(복수형)을 "할 일 목록"으로 설정

    def __str__(self):
        return self.title  # 객체를 문자열로 표시할 때 제목을 반환