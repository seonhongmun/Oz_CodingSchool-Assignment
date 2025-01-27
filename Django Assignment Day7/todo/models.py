from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image
from pathlib import Path
from io import BytesIO


User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    thumbnail = models.ImageField(
        upload_to = 'todo/thumbnails', default='todo/no_image/NO-IMAGE.gif', null=True, blank=True,
    )
    completed_image = models.ImageField(
        upload_to='todo/completed_images', null=True, blank=True,
        verbose_name="썸네일"
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

    def save(self, *args, **kwargs):
        if not self.completed_image:
            return super().save(*args, **kwargs)

        image = Image.open(self.completed_image)
        image.thumbnail((100,100))

        image_path = Path(self.completed_image.name)

        thumbnail_name = image_path.stem
        thumbnail_extension = image_path.suffix
        thumbnail_filename = f'{thumbnail_name}_thumbnail{thumbnail_extension}'

        if thumbnail_extension in ['.jpg','.jpeg']:
            file_type = 'JPEG'
        elif thumbnail_extension == '.png':
            file_type = 'PNG'
        elif thumbnail_extension == '.gif':
            file_type = 'GIF'
        else:
            return super().save(*args, **kwargs)

        temp_thumb = BytesIO()
        image.save(temp_thumb, format=file_type)
        temp_thumb.seek(0)

        if self.thumbnail and self.thumbnail.name != 'todo/no_image/NO-IMAGE.gif':
            self.thumbnail.delete(save=False)

        self.thumbnail.save(thumbnail_filename, temp_thumb, save=False)

        temp_thumb.close()
        return super().save(*args, **kwargs)


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.message}'

