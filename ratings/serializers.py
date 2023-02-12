from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Rating
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'stars', 'created_at', 'updated_at', 'movie'
        ]


class RatingDetailSerializer(RatingSerializer):
    
    rating = serializers.ReadOnlyField(source='rating.id')