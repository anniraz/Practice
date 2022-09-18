from rest_framework import serializers
from apps.user.tasks import send_message

from apps.user.models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','avatar','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        send_message.delay(validated_data['email'])
        return user
    
class UserSerializerList(serializers.ModelSerializer):
     class Meta:
        model=User
        fields=['username','last_action','avatar','email']

class VisitsCountSerializers(serializers.ModelSerializer):
    class Meta:
        model=Visits
        fields=['count','day']
        read_only_fields=('count','day')