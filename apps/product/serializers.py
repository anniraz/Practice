from rest_framework import serializers
# from rest_framework.response import Response


from apps.product.models import *
from apps.user.models import User

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=['date','name','category','price','image','description','user']
        read_only_fields=('user',)