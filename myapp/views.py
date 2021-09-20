from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django_filters.rest_framework import filters
from rest_framework import viewsets
from .models import *
from .serializer import *
from django.forms import ModelForm
# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = LocalCompany.objects
    serializer_class = LocalSerializer


class LocalXViewSet(viewsets.ModelViewSet):
    queryset = LocalCompany.objects.all()
    serializer_class = LocalXSerializer


class TraderViewSet(viewsets.ModelViewSet):
    queryset = TradeCompany.objects.all()
    serializer_class = TraderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

class TraderXViewSet(viewsets.ModelViewSet):
    queryset = TradeCompany.objects.all()
    serializer_class = TraderXSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupXViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupXSerializer


class ItemXViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemXSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class SellDetailViewSet(viewsets.ModelViewSet):
    queryset = SellDetail.objects.all()
    serializer_class = SellDetailSerializer


class SellXDetailViewSet(viewsets.ModelViewSet):
    queryset = SellDetail.objects.all()
    serializer_class = SellXDetailSerializer


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class SellXViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all().order_by('-datetime')
    serializer_class = SellXSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group','local_id','date']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class OrderXViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-datetime')
    serializer_class = OrderXSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']


class OrderedViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderedSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all().order_by('-datetime')
    serializer_class = BankSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

class PayViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaySerializer

class BuyViewSet(viewsets.ModelViewSet):
    queryset = buy.objects.all()
    serializer_class = BuySerializer

class PayLoanViewSet(viewsets.ModelViewSet):
    queryset = Payloan.objects.all()
    serializer_class = PayLoanSerializer

class ReSellViewSet(viewsets.ModelViewSet):
    queryset = ReSell.objects.all()
    serializer_class = ReSellSerializer
