from rest_framework import serializers

from .models import Games


class GamesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Games
        fields = '__all__'
