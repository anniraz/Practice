from rest_framework import viewsets,status,generics
from rest_framework.response import Response
from apps.product.models import *

from apps.user.models import *
from apps.user.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializerList

    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return UserSerializerList
        return UserSerializers
    



 