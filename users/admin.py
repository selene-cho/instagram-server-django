from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin # admin 에 있는거 가져옴 

@admin.register(User)
class CustomUserAdmin(UserAdmin): # 이미 UserAdmin 있기 때문에 Custom 붙여서 새로 만들기
    fieldsets = (
      ("Personal info"), {"fields": 
          ("username","password","email","profileIntroduce","followerNum","profileImg")}),
    list_display = (
      "username",
      "profileIntroduce",
      "followerNum",
    )
