from django.urls import path, include
from rest_framework import routers, views
from .views import *
# Routers provide an easy way of automatically determining the URL conf.
router=routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemXViewSet)
router.register(r'item', ItemViewSet)
router.register(r'sale', SellDetailViewSet)
router.register(r'sales', SellXDetailViewSet)
router.register(r'sell', SellViewSet)
router.register(r'sells', SellXViewSet)
router.register(r'local', LocalViewSet)
router.register(r'locals', LocalXViewSet)
router.register(r'trader', TraderViewSet)
router.register(r'traders', TraderXViewSet)
router.register(r'group', GroupViewSet)
router.register(r'groups', GroupXViewSet)
router.register(r'region', RegionViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orders', OrderXViewSet)
router.register(r'ordered', OrderedViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'bank', BankViewSet)
router.register(r'payment', PayViewSet)
router.register(r'payloan', PayLoanViewSet)
router.register(r'resell', ReSellViewSet)
router.register(r'buy', BuyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
