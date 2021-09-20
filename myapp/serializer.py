# Serializers define the API representation.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'
    


class TraderXSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeCompany
        fields = ['id', 'name', 'code', 'exchange', 'group',
                  'mawe', 'totallLoan', 'date', 'totallBuy']


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeCompany
        fields = '__all__'


class SellDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellDetail
        fields = '__all__'


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class LocalXSerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    totallSell = serializers.ReadOnlyField()
    attempts = serializers.SerializerMethodField()
    payment_company = PaySerializer(read_only=True, many=True)

    class Meta:
        model = LocalCompany
        fields = ['id', 'name', 'phone', 'code', 'region',
                  'owner_name', 'totallSell', 'mawe', 'totallPay', 'exchange', 'totallSellback', 'attempts', 'payment_company']
    def get_attempts(self, obj):
        quiztakers = Sell.objects.filter(local=obj)
        return SellSerializer(quiztakers, many=True).data

class SellXDetailSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(source='item.name')
    item_wight = serializers.ReadOnlyField(source='item.wight')
    item_quantity = serializers.ReadOnlyField(source='item.quantity')
    item_wightAll = serializers.ReadOnlyField(source='item.wightAll')
    item_code = serializers.ReadOnlyField(source='item.barcode')
    item_bag = serializers.ReadOnlyField(source='item.bag')
    sell = serializers.ReadOnlyField(source='sell.id')

    class Meta:
        model = SellDetail
        fields = ['id', 'item_id', 'item', 'item_code', 'item_bag',
                  'quantity', 'price', 'sell', 'date', 'total', 'item_wight', 'item_quantity', 'item_wightAll']


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalCompany
        fields = '__all__'


class ReSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReSell
        fields = '__all__'


class SellXSerializer(serializers.ModelSerializer):
    local_id = serializers.ReadOnlyField(source='local.id')
    local_name = serializers.ReadOnlyField(source='local.name')
    local_code = serializers.ReadOnlyField(source='local.code')
    local_phone = serializers.ReadOnlyField(source='local.phone')
    local_mawe = serializers.ReadOnlyField(source='local.mawe')
    local_region = serializers.ReadOnlyField(source='local.region.name')
    group_name = serializers.ReadOnlyField(source='group.name')
    vendor_name = serializers.ReadOnlyField(source='vendor.name')
    group_phone = serializers.ReadOnlyField(source='group.phone')
    vendor_phone = serializers.ReadOnlyField(source='vendor.phone')
    sell_detail = SellXDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Sell
        fields = ['id', 'url', 'local_id', 'local_name', 'local_code', 'sell_detail', 'date', 'datetime', 'totall', 'totallint', 'totalback',
                  'discount', 'group_name', 'group', 'vendor', 'vendor_name', 'group_phone', 'vendor_phone', 'local_phone', 'local_mawe', 'local_region']

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class BuySerializer(serializers.ModelSerializer):

    class Meta:
        model = buy
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Bank
        fields = ['id', 'income', 'loan', 'group', 'group_name']


class PayLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payloan
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderedSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderedXSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(source='item.name')
    item_wight = serializers.ReadOnlyField(source='item.wight')
    item_quantity = serializers.ReadOnlyField(source='item.quantity')
    # wightAll
    item_wightAll = serializers.ReadOnlyField(source='item.wightAll')
    item_code = serializers.ReadOnlyField(source='item.barcode')
    item_bag = serializers.ReadOnlyField(source='item.bag')
    sell = serializers.ReadOnlyField(source='sell.id')

    class Meta:
        model = OrderDetail
        fields = ['id', 'item', 'item_code', 'item_bag',
                  'quantity', 'price', 'sell', 'date', 'total', 'item_wight', 'item_quantity', 'item_wightAll']


class OrderXSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')
    trader_name = serializers.ReadOnlyField(source='trader.name')
    trader_mawe = serializers.ReadOnlyField(source='trader.mawe')
    order_detail = OrderedXSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ['id', 'group', 'trader', 'code',
                  'discount', 'date', 'order_detail', 'group_name', 'trader_name', 'totallint', 'totall', 'trader_mawe']


class ItemXSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source='group.name')
    trader = serializers.ReadOnlyField(source='trader.name')

    class Meta:
        model = Item
        fields = ['id', 'name', 'group', 'bag', 'quantity',
                  'barcode', 'trader', 'finalprice', 'mawe', 'wight', 'wightAll', 'price', 'addprice']


class GroupXSerializer(serializers.ModelSerializer):
    sell_group = SellXSerializer(read_only=True, many=True)
    item_group = ItemXSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'phone', 'sell_group', 'item_group']


class KashHasb(serializers.ModelSerializer):
    sell_group = SellXSerializer(read_only=True, many=True)
    item_group = ItemXSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'phone', 'sell_group', 'item_group']
