from rest_framework import serializers
from movies.models import Movie
from ratings.models import Rating

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_movie(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image for movie larger than 2MB!')
        if value.image.heigt > 4096:
            raise serializers.ValidationError('Image height for movie larger than 4096px')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width for movie larger than 4096px')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Movie
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 
            'created_at', 'updated_at', 'title', 'description', 'image', 'movie_genre_filter',
        ]
        
        