from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import UserFeedSerializer

class ReviewSerializer(ModelSerializer):
    user = UserFeedSerializer(read_only=True)
  
    class Meta:
        model = Review
        fields = (
          "user",
          "caption",
          "likesNum"
        )

