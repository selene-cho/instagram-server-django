from django.db import models
from common.models import CommonModel

# Review
# - USER (사용자)
# - FEED

# - caption: 댓글 내용

class Review(CommonModel):
    caption = models.CharField(max_length=150, default="")
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)
    
    
