from rest_framework import serializers
from accounts.models import User


class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Accounts
        fields = '__all__'