from django.urls import path
from .views import AllFeeds, DetailFeeds

urlpatterns = [
    path("", AllFeeds.as_view()),
    path("detail", DetailFeeds.as_view())
    # path("<int:feed_id>", views.FeedDetail.as_view())
    # path("<str:username>", FeedsByUsername.as_view())
]
