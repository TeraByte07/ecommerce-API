from rest_framework import serializers
from .models import User,profile,address
class userSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email',)
        model = User

class profileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'firstName', 'lastName', 'phoneNumber',)
        model = profile
        
class addressSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'streetAddress', 'city', 'zipCode',)
        model = address