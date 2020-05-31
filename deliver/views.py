from django.shortcuts import render
from django.contrib.auth.models import User
from deliver.models import Account, Cat, Dliver, Food, Request, RequestDetail, Specify, Transport, Dipricing
from rest_framework import viewsets
import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import files
from io import BytesIO
import requests

# Create your views here.


def index(request):
    context = {
        'title': "Dashboard",
    }
    return render(request, 'deliver/screens/home.html', context)


def cat(request):
    cats = Cat.objects.all()
    context = {
        'cats': cats,
        'title': "Parent Food",
    }
    return render(request, 'deliver/screens/cats.html', context)


def catDetail(request, pk):
    cats = Cat.objects.get(id=pk)
    context = {
        'cat': cats,
        'title': "Parent Food",
    }
    return render(request, 'deliver/screens/catDetail.html', context)


def catEdit(request, pk):
    cats = Cat.objects.get(id=pk)
    context = {
        'cat': cats,
        'title': "Parent Food",
    }
    return render(request, 'deliver/screens/catEdit.html', context)


def foods(request):
    cats = Cat.objects.all()
    foods = Food.objects.all()
    foodz = Food.objects.filter(deleted=False)
    context = {
        'cats': cats,
        'foods': foods,
        'foodz': foodz,
        'title': "Child Food",
    }
    return render(request, 'deliver/screens/foods.html', context)


def foodEdit(request, pk):
    foods = Food.objects.get(id=pk)
    cats = Cat.objects.filter(deleted=False)
    context = {
        'cats': cats,
        'food': foods,
        'title': "Food",
    }
    return render(request, 'deliver/screens/foodEdit.html', context)

def foodDetail(request, pk):
    foods = Food.objects.get(id=pk)
    context = {
        'food': foods,
        'title': "Food Detail",
    }
    return render(request, 'deliver/screens/foodDetail.html', context)


def disprices(request):
    disprices = Dipricing.objects.all()
    foods = Food.objects.filter(deleted=False)
    context = {
        'foods': foods,
        'disprices': disprices,
        'title': "Dipricing Food",
    }
    return render(request, 'deliver/screens/disprice.html', context)

def specifies(request):
    specifies = Specify.objects.all()
    foods = Food.objects.filter(deleted=False)
    context = {
        'foods': foods,
        'specifies': specifies,
        'title': "Specifies of Food",
    }
    return render(request, 'deliver/screens/specify.html', context)

def delivers(request):
    delivers = Dliver.objects.all()
    context = {
        'delivers': delivers,
        'title': "Delivers of Food",
    }
    return render(request, 'deliver/screens/delivers.html', context)

@csrf_exempt
def ajax(request):
    data = {
        'message': 'failed'
    }
    if request.GET.get('action') == 'spdelete':
        id = request.GET.get('id')
        sp = Specify.objects.get(pk=id)
        sp.delete()
        data = {
            'message': sp.id
        }
        return redirect('deliver:specifies')
    if request.GET.get('action') == 'disdelete':
        id = request.GET.get('id')
        dis = Dipricing.objects.get(pk=id)
        dis.delete()
        data = {
            'message': dis.id
        }
        return redirect('deliver:disprice')
    if request.GET.get('action') == 'catdelete':
        id = request.GET.get('id')
        cat = Cat.objects.get(pk=id)
        cat.deleted = not cat.deleted
        cat.save()
        data = {
            'message': cat.deleted
        }
        return redirect('deliver:cats')
    if request.GET.get('action') == 'fooddelete':
        id = request.GET.get('id')
        food = Food.objects.get(pk=id)
        food.deleted = not food.deleted
        food.save()
        data = {
            'message': food.deleted
        }
        return redirect('deliver:foods')
    if request.method == 'POST':
        if request.POST.get('action') == 'add_cat':
            cat = Cat()
            cat.nameKu = request.POST.get('nameKu')
            cat.nameEg = request.POST.get('nameEg')
            cat.image = request.FILES['images']
            cat.save()
            data = {
                'redirect': '/cats/',
                'message': 'success'
            }

        elif request.POST.get('action') == 'cat_edit':
            id = request.POST.get('id')
            cat = Cat.objects.get(pk=id)
            cat.nameKu = request.POST.get('nameKu')
            cat.nameEg = request.POST.get('nameEg')
            image = request.FILES.get('images', False)
            if image:
                cat.image = request.FILES.get('images')
            cat.save()
            data = {
                'redirect': '/catDetail/'+id,
                'message': 'seccess'
            }
        if request.POST.get('action') == 'food_add':
            food = Food()
            food.category_id = int(request.POST.get('catId'))
            food.title = request.POST.get('title')
            food.subtitle = request.POST.get('subtitle')
            food.detiles = request.POST.get('detiles')
            food.sell_price = request.POST.get('sell_price')
            food.cost = request.POST.get('cost')
            food.image = request.FILES['images']
            food.save()
            data = {
                'redirect': '/foods/',
                'message': 'success'
            }
        if request.POST.get('action') == 'food_edit':
            id = request.POST.get('id')
            food = Food.objects.get(pk=id)
            food.category_id = int(request.POST.get('catId'))
            food.title = request.POST.get('title')
            food.subtitle = request.POST.get('subtitle')
            food.detiles = request.POST.get('detiles')
            food.sell_price = request.POST.get('sell_price')
            food.cost = request.POST.get('cost')
            image = request.FILES.get('images', False)
            if image:
                food.image = request.FILES['images']
            food.save()
            data = {
                'redirect': '/foods/',
                'message': 'success'
            }
        if request.POST.get('action') == 'specify':
            sp = Specify()
            sp.food_id = request.POST.get('foodId')
            sp.title = request.POST.get('title')
            sp.price = request.POST.get('price')
            sp.save()
            data = {
                'redirect': '/specifies/',
                'message': 'success'
            }
        if request.POST.get('action') == 'disprice':
            dp = Dipricing()
            dp.food_id = request.POST.get('foodId')
            dp.title = request.POST.get('title')
            dp.price = request.POST.get('price')
            dp.start_date = request.POST.get('start_date')
            dp.exp_date = request.POST.get('exp_date')
            dp.save()
            data = {
                'redirect': '/disprices/',
                'message': 'success'
            }
    return JsonResponse(data)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializer.UserSerializer

# ViewSets define the view behavior.


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = serializer.CatSerializer

# ViewSets define the view behavior.


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = serializer.FoodSerializer


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = serializer.FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_id']


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
