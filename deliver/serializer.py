# from django.contrib.auth.models import User
from . import models
from rest_framework import serializers
from deliver.models import RequestDetail, Specify

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Account
        fields = ['id', 'url', 'username', 'email', 'is_staff']

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cat
        fields = ['id', 'url', 'image', 'nameEg', 'nameKu', 'detiles','date_added']

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Food
        fields = ['id', 'url', 'category', 'category_id', 'image', 'price', 'disprice', 'title', 'subtitle', 'detiles','date_added', 'is_dispriced']

class SpecifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Specify
        fields = ['id','food','title','date_added','food_id']

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    request_detail = serializers.PrimaryKeyRelatedField(many=True, queryset= RequestDetail.objects.all())
    class Meta:
        model = models.Request
        fields = ['id', 'name', 'phone', 'address','total_price', 'request_detail','phoneid']

class RequestDetailSerializer(serializers.HyperlinkedModelSerializer):
    food = serializers.CharField(source='food_id')
    food_title =  serializers.ReadOnlyField(source='food.title')
    specify = serializers.PrimaryKeyRelatedField(many=True, queryset= Specify.objects.all())
    class Meta:
        model = models.RequestDetail
        fields = ['id','food', 'food_title', 'quantity', 'specify','total_price','phoneid','date_added','last_edit', 'status']

class DliverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Dliver
        fields = ['id', 'name', 'user']

class TransportSerializer(serializers.HyperlinkedModelSerializer):
    dliver_name =  serializers.ReadOnlyField(source='dliver.name')
    request_name =  serializers.ReadOnlyField(source='request.name')
    request_total_price = serializers.ReadOnlyField(source='request.total_price')
    request_phoneid =  serializers.ReadOnlyField(source='request.phoneid')
    request_phone =  serializers.ReadOnlyField(source='request.phone')
    request_address =  serializers.ReadOnlyField(source='request.address')

    class Meta:
        model = models.Transport
        fields = ['id', 'dliver', 'request', 'start_date', 'end_date', 'status','dliver_name', 'request_name','request_phoneid', 'request_phone','request_id','dliver_id','request_total_price','request_address']