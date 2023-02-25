from django.urls import path
from .views import AllFeeds, FeedsDetail, FeedsByUsername

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("detail", FeedsDetail.as_view()),
    path("<str:username>", FeedsByUsername.as_view()),
    # path("<int:feed_id>", FeedsDetail.as_view()),
    
]
