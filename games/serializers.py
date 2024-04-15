from rest_framework import serializers

from .models import Games


class GamesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Games
        fields = ('id', 'title', 'description', 'controller',
                  'rating', 'time_create', 'user', 'cat')
