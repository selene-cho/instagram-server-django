from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer

# 전체 feed 데이터 모두 보여주는 Serializer
class FeedSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Feed
        fields = "__all__" # Model 전체 field 가져오기
        depth = 1 # objects도 serialize화 시킴.
        
        
class FeedDetailSerializer(ModelSerializer): # 일부 데이터 보여주는 Serializer
    user = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = ("id","user","caption","likesNum", "reviews")



# class FeedDetailSerializer(ModelSerializer): 
#     user = FeedUserSerializer(read_only=True) # 유저한테서 유저정보를 입력받으면 안됨.
#     review_set = FeedReviwsSerializer(many=True, read_only=True)
#     class Meta:
#         model = Feed
#         fields = "__all__"