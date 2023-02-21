from django.db import models
from django.contrib.auth.models import AbstractUser


# username: 유저이름 => 기존 admin에 이미 포함되어 있어서 생성하지 않아도 됨
# profileIntroduce : 유저 프로필 소개글
# profileImg : 유저 프로필 이미지
# followerNum : 유저 팔로워 수

class User(AbstractUser):
  profileImg = models.URLField(blank=True) # 이미지 링크 첨부하기 위함(이미지 쓰는 경우 URLField 가져오면 됨.)
  profileIntroduce = models.CharField(max_length=150, default="")
  followerNum = models.PositiveIntegerField(default=0)  

