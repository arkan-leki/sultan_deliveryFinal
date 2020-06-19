# from django.contrib.auth.models import User
from . import models
from rest_framework import serializers
from deliver.models import RequestDetail, Specify

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Account
        fields = ['id', 'url', 'username', 'email', 'is_staff']

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cat
        fields = ['id', 'image', 'nameEg', 'nameKu', 'deleted','date_added']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ['id', 'category', 'category_id', 'image', 'sell_price', 'title', 'subtitle', 'detiles','date_add', 'deleted', 'cost']

class SpecifySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specify
        fields = ['id','food','title', 'price','date_added','food_id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'name', 'password', 'instrument_purchase','house_no','address_line1', 'address_line2', 'phone', 'phoneid', 'zip_code', 'country', 'image']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rate
        fields = ['id', 'food','customer', 'stars']

class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motors
        fields = ['id', 'title','number', 'image', 'status']

class SpecifySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specify
        fields = ['id','food','title', 'price','date_added','food_id']


class RequestSerializer(serializers.ModelSerializer):
    request_detail = serializers.PrimaryKeyRelatedField(many=True, queryset= RequestDetail.objects.all())
    class Meta:
        model = models.Request
        fields = ['id', 'name', 'phone', 'address','total_price', 'dashkandin', 'request_detail','customer', 'date_added','last_edit' , 'status']

class RequestDetailSerializer(serializers.ModelSerializer):
    food = serializers.CharField(source='food_id')
    food_title =  serializers.ReadOnlyField(source='food.title')
    specify = serializers.PrimaryKeyRelatedField(many=True, queryset= Specify.objects.all())
    class Meta:
        model = models.RequestDetail
        fields = ['id','food', 'food_title', 'quantity', 'specify','total_price', 'dashkandin', 'customer','date_added','last_edit', 'status']

class DliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dliver
        fields = ['id', 'name', 'user', 'motor', 'phone', 'phoneId', 'image']

class TransportSerializer(serializers.ModelSerializer):
    dliver_name =  serializers.ReadOnlyField(source='dliver.name')
    request_name =  serializers.ReadOnlyField(source='request.name')
    request_total_price = serializers.ReadOnlyField(source='request.total_price')
    request_phoneid =  serializers.ReadOnlyField(source='request.phoneid')
    request_phone =  serializers.ReadOnlyField(source='request.phone')
    request_address =  serializers.ReadOnlyField(source='request.address')

    class Meta:
        model = models.Transport
        fields = ['id', 'dliver', 'request', 'start_date', 'end_date', 'status','dliver_name', 'request_name','request_phoneid', 'request_phone','request_id','dliver_id','request_total_price','request_address']