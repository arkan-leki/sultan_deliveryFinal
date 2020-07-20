# from django.contrib.auth.models import User
from rest_framework import serializers

from deliver import models
from deliver.models import RequestDetail, Specify


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:account-detail")
    class Meta:
        model = models.Account
        fields = ['id', 'username', 'email', 'is_staff']


class BnkaSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:warehouse-detail")
    class Meta:
        model = models.Warehouse
        fields = ['id', 'title', 'image', 'status', 'items']


class CatSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:cat-detail")
    # war = serializers.HyperlinkedIdentityField(view_name="api:warehouse-detail")
    class Meta:
        model = models.Cat
        fields = ['id', 'war', 'image', 'nameEg', 'nameKu', 'deleted', 'date_added']


class FoodSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:food-detail") category =
    # serializers.HyperlinkedIdentityField(view_name="api:cat-detail") disprice = serializers.PrimaryKeyRelatedField(
    # many=True, queryset=Dipricing.objects.filter(exp_date__gt=datetime.now()).order_by('-exp_date'))
    popularity = serializers.CharField()
    category_war = serializers.ReadOnlyField(source='category.war_id')
    fav_food = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='customer_id'
     )

    class Meta:
        model = models.Food
        fields = ['id', 'category', 'category_war', 'image', 'sell_price', 'title', 'subtitle', 'detiles', 'date_add',
                  'deleted', 'cost', 'popularity', 'avg_ratings', 'isDispriced', 'disprice', 'dispriceTitle',
                  'dispriceId', 'dispriceDate', 'fav_food']


class SpecifySerializer(serializers.ModelSerializer):
    # food = serializers.HyperlinkedIdentityField(view_name="api:food-detail")
    # url = serializers.HyperlinkedIdentityField(view_name="api:specify-detail")
    class Meta:
        model = models.Specify
        fields = ['id', 'food', 'title', 'price', 'date_added']


class CustomerSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    fav_user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='food_id'
     )

    class Meta:
        model = models.Customer
        fields = ['id', 'name', 'password', 'instrument_purchase', 'house_no', 'address_line1', 'address_line2',
                  'phone', 'phoneid', 'zip_code', 'country', 'image', 'email', 'fav_user']


class RateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:rate-detail")
    # customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    # food = serializers.HyperlinkedIdentityField(view_name="api:food-detail")
    class Meta:
        model = models.Rate
        fields = ['id', 'food', 'customer', 'stars']


class FaveSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:favorate-detail")
    # customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    # food = serializers.HyperlinkedIdentityField(view_name="api:food-detail")

    class Meta:
        model = models.Favorate
        fields = ['id', 'food', 'customer']


class MotorSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:motor-detail")
    class Meta:
        model = models.Motors
        fields = ['id', 'title', 'number', 'image', 'status']


class RequestSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:request-detail")
    # customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    request_detail = serializers.PrimaryKeyRelatedField(many=True, queryset=RequestDetail.objects.all())

    class Meta:
        model = models.Request
        fields = ['id', 'name', 'phone', 'address', 'total_price', 'dashkandin', 'request_detail', 'customer',
                  'date_added', 'last_edit', 'status']


class RequestDetailSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:requestDetail-detail")
    # customer = serializers.HyperlinkedIdentityField(view_name="api:customer-detail")
    food = serializers.CharField(source='food_id')
    food_title = serializers.ReadOnlyField(source='food.title')
    specify = serializers.PrimaryKeyRelatedField(many=True, queryset=Specify.objects.all())

    class Meta:
        model = models.RequestDetail
        fields = ['id', 'food', 'food_title', 'quantity', 'specify', 'total_price', 'dashkandin', 'customer',
                  'date_added', 'last_edit', 'status']


class DliverSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:deliver-detail")
    # user = serializers.HyperlinkedIdentityField(view_name="api:account-detail")
    class Meta:
        model = models.Dliver
        fields = ['id', 'name', 'user', 'motor', 'phone', 'phoneId', 'image']


class TransportSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:transport-detail")
    dliver_name = serializers.ReadOnlyField(source='dliver.name')
    request_name = serializers.ReadOnlyField(source='request.name')
    request_total_price = serializers.ReadOnlyField(source='request.total_price')
    request_phoneid = serializers.ReadOnlyField(source='request.phoneid')
    request_phone = serializers.ReadOnlyField(source='request.phone')
    request_address = serializers.ReadOnlyField(source='request.address')

    class Meta:
        model = models.Transport
        fields = ['id', 'dliver', 'request', 'start_date', 'end_date', 'status', 'dliver_name', 'request_name',
                  'request_phoneid', 'request_phone', 'request_total_price', 'request_address']
