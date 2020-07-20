from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework import viewsets

from deliver.models import Account, Cat, Customer, Dliver, Favorate, Food, Motors, Rate, Request, \
    RequestDetail, Specify, Transport, Warehouse
from . import serializer


# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializer.UserSerializer


# ViewSets define the view behavior.


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.filter(deleted=False, war__status=False)
    serializer_class = serializer.CatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'war']


# ViewSets define the view behavior.


class FoodViewSet(viewsets.ModelViewSet):
    cats = Cat.objects.filter(deleted=False, war__status=False)
    foods = Food.objects.filter(deleted=False, category__in=cats)
    queryset = foods
    serializer_class = serializer.FoodSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class FoodListView(generics.ListAPIView):
    cats = Cat.objects.filter(deleted=False, war__status=False)
    foods = Food.objects.filter(deleted=False, category__in=cats)
    queryset = foods
    serializer_class = serializer.FoodSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ['title', 'subtitle']
    filterset_fields = ['id', 'category']
    ordering_fields = ['date_add', 'rate_food', 'title']


class SpecifyListView(generics.ListAPIView):
    foods = Food.objects.filter(deleted=False)
    specifies = Specify.objects.filter(food__in=foods)
    queryset = specifies
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'phoneid']


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = serializer.RateSerializer


class FaveViewSet(viewsets.ModelViewSet):
    queryset = Favorate.objects.all()
    serializer_class = serializer.FaveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'customer', 'food']


class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motors.objects.all()
    serializer_class = serializer.MotorSerializer


class BnkaViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.filter(status=False)
    serializer_class = serializer.BnkaSerializer
