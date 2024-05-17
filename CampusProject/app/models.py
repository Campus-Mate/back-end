from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    kakao_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    # related_name 속성 추가
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # 이 부분을 추가
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # 이 부분을 추가
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
