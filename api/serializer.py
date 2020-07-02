# from django.contrib.auth.models import User
from deliver import models
from rest_framework import serializers
from deliver.models import RequestDetail, Specify, BnkaUser

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:account-detail")
    class Meta:
        model = models.Account
        fields = ['id', 'url', 'username', 'email', 'is_staff']

class BnkaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:warehouse-detail")
    class Meta:
        model = models.Warehouse
        fields = ['id', 'url', 'title', 'status']

class CatSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:cat-detail")
    war = serializers.HyperlinkedIdentityField(view_name="api:warehouse-detail")
    class Meta:
        model = models.Cat
        fields = ['id', 'url', 'war', 'war_id', 'image', 'nameEg', 'nameKu', 'deleted','date_added']

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:food-detail")
    category = serializers.HyperlinkedIdentityField(view_name="api:cat-detail")
    popularity = serializers.CharField()
    category_war =  serializers.ReadOnlyField(source='category.war_id')
    class Meta:
        model = models.Food
        fields = ['id', 'url', 'category', 'category_id', 'category_war', 'image', 'sell_price', 'title', 'subtitle', 'detiles','date_add', 'deleted', 'cost', 'popularity' , 'avg_ratings']

class SpecifySerializer(serializers.HyperlinkedModelSerializer):
    food = serializers.HyperlinkedIdentityField(view_name="api:food-detail")
    url = serializers.HyperlinkedIdentityField(view_name="api:specify-detail")
    class Meta:
        model = models.Specify
        fields = ['id', 'url', 'food','title', 'price','date_added','food_id']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    class Meta:
        model = models.Customer
        fields = ['id', 'url', 'name', 'password', 'instrument_purchase','house_no','address_line1', 'address_line2', 'phone', 'phoneid', 'zip_code', 'country', 'image']

class RateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:rate-detail")
    class Meta:
        model = models.Rate
        fields = ['id', 'url', 'food','customer', 'stars']

class MotorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:motor-detail")
    class Meta:
        model = models.Motors
        fields = ['id', 'url', 'title','number', 'image', 'status']

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:request-detail")
    customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    request_detail = serializers.PrimaryKeyRelatedField(many=True, queryset= RequestDetail.objects.all())
    class Meta:
        model = models.Request
        fields = ['id', 'url', 'name', 'phone', 'address','total_price', 'dashkandin', 'request_detail','customer', 'date_added','last_edit' , 'status']

class RequestDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:requestDetail-detail")
    customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    food = serializers.CharField(source='food_id')
    food_title =  serializers.ReadOnlyField(source='food.title')
    specify = serializers.PrimaryKeyRelatedField(many=True, queryset= Specify.objects.all())
    class Meta:
        model = models.RequestDetail
        fields = ['id', 'url', 'food', 'food_title', 'quantity', 'specify','total_price', 'dashkandin', 'customer','date_added','last_edit', 'status']

class DliverSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:deliver-detail")
    user = serializers.HyperlinkedIdentityField(view_name="api:account-detail")
    class Meta:
        model = models.Dliver
        fields = ['id', 'url', 'name', 'user', 'motor', 'phone', 'phoneId', 'image']

class TransportSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:transport-detail")
    dliver_name =  serializers.ReadOnlyField(source='dliver.name')
    request_name =  serializers.ReadOnlyField(source='request.name')
    request_total_price = serializers.ReadOnlyField(source='request.total_price')
    request_phoneid =  serializers.ReadOnlyField(source='request.phoneid')
    request_phone =  serializers.ReadOnlyField(source='request.phone')
    request_address =  serializers.ReadOnlyField(source='request.address')
    class Meta:
        model = models.Transport
        fields = ['id', 'url', 'dliver', 'request', 'start_date', 'end_date', 'status','dliver_name', 'request_name','request_phoneid', 'request_phone','request_id','dliver_id','request_total_price','request_address']