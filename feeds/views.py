from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed
from .serializers import FeedSerializer, FeedDetailSerializer

class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(all_feeds, many=True)
        
        return Response(serializer.data)


class DetailFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedDetailSerializer(all_feeds, many=True)
        
        return Response(serializer.data)

# class FeedsByUsername(APIView):
#     def get_object(self, username):
#         Feed.objects.filter()
        
#     def get(self, request, username):
#         all_feeds = Feed.objects(username)
#         serializer = FeedSerializer(all_feeds)
        
#         return Response(serializer.data)