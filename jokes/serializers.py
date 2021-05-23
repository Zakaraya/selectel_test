from rest_framework import serializers
from .models import Joke


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ('id', 'joke_text', 'add_time')