from django.db import models

class CommonModel(models.Model) : 
  created = models.DateTimeField(auto_now_add=True) # 
  updated = models.DateTimeField(auto_now=True) # 지금 현재시간 기준
  
  class Meta:
    abstract = True # DB에 테이블을 추가하지 않겠음.