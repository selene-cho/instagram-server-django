from django.db import models
from common.models import CommonModel

# Review
# - USER (사용자)
# - FEED

# - caption: 댓글 내용
# - likesNum: 좋아요 갯수

class Review(CommonModel):
    caption = models.CharField(max_length=150, default="")
    likesNum = models.PositiveIntegerField(default=0)
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    # user -> review
    # user.review_set.all() -> user.reviews.all()
    
    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE, # 게시글 지워졌을 때 댓글 지워짐
        related_name="reviews"
    )
    # feed -> review
    # feed.reviews.all()

