from django.conf.urls import url, include
from django.contrib.auth.models import User
from deliver.models import Account, Cat, Dliver, Food, Request, RequestDetail, Specify, Transport, Dipricing, Motors, Customer, Rate, Warehouse, BnkaUser
from rest_framework import routers, serializers, viewsets
from . import views
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'cats', views.CatViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'specify', views.SpecifyViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'request_details', views.RequestDetailViewSet)
router.register(r'dlivers', views.DliverViewSet)
router.register(r'transports', views.TransportViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'rates', views.RateViewSet)
router.register(r'motors', views.MotorViewSet)
router.register(r'bnka', views.BnkaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api'

urlpatterns = [
    path('account/', include("api.api.urls", namespace='deliver_api')),
    url('^requestz/$', views.RequestDetailListView.as_view()),
    url('^foodz/$', views.FoodListView.as_view()),
    url('^specifyz/$', views.SpecifyListView.as_view()),
    url(r'', include(router.urls)),
    url(r'/', include('rest_framework.urls', namespace='rest_framework')),
]