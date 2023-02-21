from django.contrib import admin
from feeds.models import Feed # 같은 폴더안에 있으니까 .models 라고 적어도 OK

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
  list_display = (
    "caption",
    "likesNum",
    "reviewsNum",
  )