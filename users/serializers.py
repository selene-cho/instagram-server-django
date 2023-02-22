from .models import User
from rest_framework.serializers import ModelSerializer

# ModelSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        
        fields = (
          "id",
          "email",
          "username",
          "profileImg",
          "profileIntroduce",
        )

class UserFeedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
          "id",
          "username",
          "email"
        )
      