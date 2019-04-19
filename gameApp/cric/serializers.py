from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from rest_framework import serializers
from .models import Newsfeed


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        fields = ("newsid", "theirid","title","itemlink","detail","imagelink","source","tags","timestamp")
