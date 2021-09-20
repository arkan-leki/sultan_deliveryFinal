from django.contrib import admin
from django.contrib.admin.decorators import display
from myapp.models import *
# Register your models here.
# admin.site.register(TradeCompany)
admin.site.register(Item)
admin.site.register(Region)
admin.site.register(Vendor)
admin.site.register(Bank)
admin.site.register(Payment)

class SelldetailAdmin(admin.TabularInline):
    model = SellDetail
    # fields = ('item','quantity','price')
    readonly_fields = ['addprice','mawe']

class SellAdmin(admin.ModelAdmin):
    model = Sell
    inlines = [SelldetailAdmin]

admin.site.register(Sell, SellAdmin)


class OrderdetailAdmin(admin.TabularInline):
    model = OrderDetail

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderdetailAdmin]

admin.site.register(Order, OrderAdmin)

admin.site.register(LocalCompany)
# admin.site.register(SellDetail)


class ItemDetailAdmin(admin.TabularInline):
    model = Item

class GroupAdmin(admin.ModelAdmin):
    model = Group
    inlines = [ItemDetailAdmin]

admin.site.register(Group, GroupAdmin)

class TradeCompanyAdmin(admin.ModelAdmin):
    model = TradeCompany
    inlines = [ItemDetailAdmin]

admin.site.register(TradeCompany, TradeCompanyAdmin)
