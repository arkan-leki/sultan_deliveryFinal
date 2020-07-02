from django.conf.urls import url, include
from . import views
from django.urls import path, include

app_name = 'deliver'

urlpatterns = [
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
    path('customers/', views.customers, name="customers"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('ajax/', views.ajax, name="ajax"),
    path('warehouse/', views.warehouse, name="warehouse"),
]
