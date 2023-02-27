from django.db import models
from common.models import CommonModel

# Feed
# - USER (사용자)

# - caption: 게시글 내용
# - contentImg : 게시글 이미지
# - likesNum : 좋아요 갯수
# - reviewsNum : 댓글 갯수

class Feed(CommonModel):
    caption = models.CharField(max_length=1000, default="") # 게시글 내용
    contentImg = models.URLField(blank=True, null=True) # 게시글 이미지
    likesNum = models.PositiveIntegerField(default=0) # 좋아요 갯수
    reviewsNum = models.PositiveIntegerField(default=0) # 댓글 갯수
    
    # 1:N (User:Feed), N이 ForeignKey를 갖음.
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE, # 유저삭제시 CASCADE: 게시글삭제
        related_name="feeds" # revers accesor에서 불러올 이름(users.feed_set.all() = users.feeds.all(): 유저가 본인이 작성한 게시물 모두 가져올 때 원래 왼쪽처럼 작성하는 것을 feeds로 바꿔서 오른쪽 처럼 불러올 수 있게함)
    )

    def __str__(self) -> str: # admin 페이지에서 문자열 caption으로 보이게
        return self.caption