from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Feed
from users.models import User
from .serializers import FeedSerializer, FeedsDetailSerializer

# 전체 게시글 불러오는 API
class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(all_feeds, many=True)
        
        return Response(serializer.data)


class FeedsDetail(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedsDetailSerializer(feeds, many=True)
        
        return Response(serializer.data)

# username 기반으로 특정 유저의 게시글을 불러오는 API
class FeedsByUsername(APIView):
    def get_object(self, username):
        try:
            user = User.objects.get(username = username)
            print("username", username)
            print("user_id", user.id)
            
            user_feeds = Feed.objects.filter(user_id=user.id)
            print("user_feeds", user_feeds)
            return user_feeds
        
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, username):
        feeds = self.get_object(username)
        serializer = FeedsDetailSerializer(feeds, many=True)
        
        return Response(serializer.data)