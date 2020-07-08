from django.shortcuts import render
from rest_framework import viewsets
from deliver.models import Account, BnkaUser, Cat, Customer, Dipricing, Dliver, Favorate, Food, Motors, Rate, Request, RequestDetail, Specify, Transport, Warehouse
from . import serializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializer.UserSerializer

# ViewSets define the view behavior.


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.filter(deleted=False)
    serializer_class = serializer.CatSerializer

# ViewSets define the view behavior.


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(deleted=False)
    serializer_class = serializer.FoodSerializer


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.filter(deleted=False)
    serializer_class = serializer.FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'category_id']


class SpecifyListView(generics.ListAPIView):
    queryset = Specify.objects.all()
    serializer_class = serializer.SpecifySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['food_id']

# ViewSets define the view behavior.


class SpecifyViewSet(viewsets.ModelViewSet):
    queryset = Specify.objects.all()
    serializer_class = serializer.SpecifySerializer

# ViewSets define the view behavior.


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = serializer.RequestSerializer

# ViewSets define the view behavior.


class RequestDetailViewSet(viewsets.ModelViewSet):
    queryset = RequestDetail.objects.all()
    serializer_class = serializer.RequestDetailSerializer

# ViewSets define the view behavior.


class DliverViewSet(viewsets.ModelViewSet):
    queryset = Dliver.objects.all()
    serializer_class = serializer.DliverSerializer


class RequestDetailListView(generics.ListAPIView):
    queryset = RequestDetail.objects.all()
    serializer_class = serializer.RequestDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phoneid', 'status']

# ViewSets define the view behavior.


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = serializer.TransportSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializer.CustomerSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = serializer.RateSerializer

class FaveViewSet(viewsets.ModelViewSet):
    queryset = Favorate.objects.all()
    serializer_class = serializer.FaveSerializer

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motors.objects.all()
    serializer_class = serializer.MotorSerializer

class BnkaViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = serializer.BnkaSerializer
