from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('생성일', auto_now_add=True) #생성시 현재 시간 자동 저장
    updated_at = models.DateTimeField('수정일', auto_now=True) #수정시 현재 시간 자동 업데이트

    class Meta:
        abstract = True