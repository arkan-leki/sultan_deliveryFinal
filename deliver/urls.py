from django.conf.urls import url, include
from django.contrib.auth.models import User
from deliver.models import Cat
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

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'deliver'

urlpatterns = [
    path('api/account/', include("deliver.api.urls", namespace='deliver_api')),

    path('', views.index, name="home"),
    path('cats/', views.cat, name="cats"),
    path('catEdit/<pk>', views.catEdit, name="catEdit"),
    path('catDetail/<pk>', views.catDetail, name="catDetail"),
    path('foods/', views.foods, name="foods"),
    path('foodEdit/<pk>', views.foodEdit, name="foodEdit"),
    path('foodDetail/<pk>', views.foodDetail, name="foodDetail"),
    path('disprices/', views.disprices, name="disprice"),
    path('specifies/', views.specifies, name="specifies"),
    path('delivers/', views.delivers, name="delivers"),
    path('deliverEdit/<pk>', views.deliverEdit, name="deliverEdit"),
    path('motors/', views.motors, name="motors"),
    path('transports/', views.transports, name="transports"),
    path('motorEdit/<pk>', views.motorEdit, name="motorEdit"),
    path('accounts/', views.accounts, name="accounts"),
    path('requests/', views.requests, name="requests"),
    path('requestDetail/', views.requestDetail, name="requestDetail"),
    path('requestView/<pk>', views.requestView, name="requestView"),
    path('requestDetailView/<pk>', views.requestDetailView, name="requestDetailView"),
    path('customer/<pk>', views.customer, name="customer"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('ajax/', views.ajax, name="ajax"),

    url('^api/requestz/$', views.RequestDetailListView.as_view()),
    url('^api/foodz/$', views.FoodListView.as_view()),
    url('^api/specifyz/$', views.SpecifyListView.as_view()),
    url(r'^api/', include((router.urls, 'deliver'), namespace='deliver')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
