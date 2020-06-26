from django.shortcuts import render
from django.contrib.auth.models import User
from deliver.models import Account, Cat, Dliver, Food, Request, RequestDetail, Specify, Transport, Dipricing, Motors, Customer, Rate, Warehouse, BnkaUser
from rest_framework import viewsets
from . import serializer
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
from deliver.forms import UserForm
import datetime

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    context = {
        'title': "Dashboard",
    }
    return render(request, 'deliver/screens/home.html', context)

def loginView(request):
    context = {
        'title': "Login",
    }
    return render(request, 'deliver/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('deliver:home')

@login_required(login_url='/login/')
def cat(request):
    user = request.user
    if user.is_staff:
        war = Warehouse.objects.all()
        cats = Cat.objects.all()
        context = {
            'warehouses': war,
            'cats': cats,
            'title': "Parent Food",
        }
    else:
        for bnkas in user.BnkasUser.all():
            bnka = bnkas.bnka
        war = Warehouse.objects.filter(id=bnka.id)
        cats = Cat.objects.filter(war=bnka.id)
        context = {
            'warehouses': war,
            'cats': cats,
            'title': "Parent Food",
        }
    return render(request, 'deliver/screens/cats.html', context)


@login_required(login_url='/login/')
def catDetail(request, pk):
    cats = Cat.objects.get(id=pk)
    context = {
        'cat': cats,
        'title': "Parent Food",
    }
    return render(request, 'deliver/screens/catDetail.html', context)

@login_required(login_url='/login/')
def catEdit(request, pk):
    war = Warehouse.objects.all()
    cats = Cat.objects.get(id=pk)
    context = {
        'warehouses': war,
        'cat': cats,
        'title': "Parent Food",
    }
    return render(request, 'deliver/screens/catEdit.html', context)

@login_required(login_url='/login/')
def foods(request):
    user = request.user
    if user.is_staff:
        cats = Cat.objects.filter(deleted=False)
        foods = Food.objects.all()
        foodz = Food.objects.filter(deleted=False)
        context = {
            'cats': cats,
            'foods': foods,
            'foodz': foodz,
            'title': "Child Food",
        }
    else:
        for bnkas in user.BnkasUser.all():
            bnka = bnkas.bnka
        cats = Cat.objects.filter(deleted=False, war=bnka.id)
        foods = Food.objects.filter(warehouse=bnka.id)
        foodz = Food.objects.filter(deleted=False, warehouse=bnka.id)
        context = {
            'cats': cats,
            'foods': foods,
            'foodz': foodz,
            'title': "Child Food",
        }
    return render(request, 'deliver/screens/foods.html', context)

@login_required(login_url='/login/')
def foodEdit(request, pk):
    foods = Food.objects.get(id=pk)
    cats = Cat.objects.filter(deleted=False)
    context = {
        'cats': cats,
        'food': foods,
        'title': "Food",
    }
    return render(request, 'deliver/screens/foodEdit.html', context)

@login_required(login_url='/login/')
def foodDetail(request, pk):
    foods = Food.objects.get(id=pk)
    context = {
        'food': foods,
        'title': "Food Detail",
    }
    return render(request, 'deliver/screens/foodDetail.html', context)

@login_required(login_url='/login/')
def disprices(request):
    disprices = Dipricing.objects.all()
    foods = Food.objects.filter(deleted=False)
    context = {
        'foods': foods,
        'disprices': disprices,
        'title': "Dipricing Food",
    }
    return render(request, 'deliver/screens/disprice.html', context)

@login_required(login_url='/login/')
def specifies(request):
    specifies = Specify.objects.all()
    if request.user.is_staff:
        foods = Food.objects.filter(deleted=False)
    else:
        for bnkas in request.user.BnkasUser.all():
            bnka = bnkas.bnka
        foods = Food.objects.filter(deleted=False, warehouse=bnka.id)
    context = {
        'foods': foods,
        'specifies': specifies,
        'title': "Specifies of Food",
    }
    return render(request, 'deliver/screens/specify.html', context)

@login_required(login_url='/login/')
def transports(request):
    transports = Transport.objects.all()
    context = {
        'transports': transports,
        'title': "transports of Request",
    }
    return render(request, 'deliver/screens/transports.html', context)

@login_required(login_url='/login/')
def delivers(request):
    delivers = Dliver.objects.all()
    users = Account.objects.all()
    motors = Motors.objects.all()
    context = {
        'users': users,
        'motors': motors,
        'delivers': delivers,
        'title': "Delivers of Food",
    }
    return render(request, 'deliver/screens/delivers.html', context)

@login_required(login_url='/login/')
def deliverEdit(request, pk):
    delivers = Dliver.objects.all()
    users = Account.objects.all()
    motors = Motors.objects.all()
    deliver = Dliver.objects.get(id=pk)
    context = {
        'users': users,
        'deliver': deliver,
        'motors': motors,
        'delivers': delivers,
        'title': "Deliver Edit",
    }
    return render(request, 'deliver/screens/delivers.html', context)

@login_required(login_url='/login/')
def motors(request):
    motors = Motors.objects.all()
    context = {
        'motors': motors,
        'title': "Motors",
    }
    return render(request, 'deliver/screens/motors.html', context)

@login_required(login_url='/login/')
def motorEdit(request, pk):
    motor = Motors.objects.get(id=pk)
    motors = Motors.objects.all()
    context = {
        'motors': motors,
        'motor': motor,
        'title': "Motors Edit",
    }
    return render(request, 'deliver/screens/motors.html', context)

@login_required(login_url='/login/')
def accounts(request):
    war = Warehouse.objects.all()
    accounts = Account.objects.all()
    context = {
        'war': war,
        'userform': UserForm,
        'accounts': accounts,
        'title': "Accounts",
    }
    return render(request, 'deliver/screens/accounts.html', context)

@login_required(login_url='/login/')
def warehouse(request):
    ls = Warehouse.objects.all()
    context = {
        'userform': UserForm,
        'warehouses': ls,
        'title': "Warehouse",
    }
    return render(request, 'deliver/screens/warehouse.html', context)

@login_required(login_url='/login/')
def requestDetail(request):
    requests = RequestDetail.objects.all()
    context = {
        'requests': requests,
        'title': "Requests of Food",
    }
    return render(request, 'deliver/screens/requestDetail.html', context)

@login_required(login_url='/login/')
def requestDetailView(request,pk):
    f = RequestDetail.objects.get(id=pk)
    context = {
        'request': f,
        'title': "Requests of Food",
    }
    return render(request, 'deliver/screens/RequestDetailView.html', context)

@login_required(login_url='/login/')
def requestView(request,pk):
    f = Request.objects.get(id=pk)
    context = {
        'request': f,
        'title': "Requests of Food",
    }
    return render(request, 'deliver/screens/RequestView.html', context)

@login_required(login_url='/login/')
def customer(request,pk):
    f = Customer.objects.get(id=pk)
    context = {
        'customer': f,
        'title': "Customer",
    }
    return render(request, 'deliver/screens/customer.html', context)

@login_required(login_url='/login/')
def customers(request):
    f = Customer.objects.all()
    context = {
        'customers': f,
        'title': "Customers",
    }
    return render(request, 'deliver/screens/customers.html', context)

@login_required(login_url='/login/')
def requests(request):
    dlivers = Dliver.objects.all()
    requests = Request.objects.all()
    context = {
        'requests': requests,
        'dlivers': dlivers,
        'title': "Detail Delivery of Request",
    }
    return render(request, 'deliver/screens/requests.html', context)

@csrf_exempt
def ajax(request):
    data = {
        'message': 'failed'
    }
    if request.GET.get('action') == 'motordelete':
        id = request.GET.get('id')
        db = Motors.objects.get(pk=id)
        db.delete()
        data = {
            'message': 'deleted'
        }
        return redirect('deliver:motors')
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
    if request.GET.get('action') == 'catremove':
        id = request.GET.get('id')
        cat = Cat.objects.get(pk=id)
        cat.delete()
        data = {
            'message': "deleted"
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
    if request.GET.get('action') == 'motordelete':
        id = request.GET.get('id')
        sp = Motors.objects.get(pk=id)
        sp.delete()
        data = {
            'message': sp.id
        }
        return redirect('deliver:motors')
    if request.GET.get('action') == 'deliverdelete':
        id = request.GET.get('id')
        sp = Dliver.objects.get(pk=id)
        sp.delete()
        data = {
            'message': sp.id
        }
        return redirect('deliver:delivers')
    if request.GET.get('action') == 'warehousedelete':
        id = request.GET.get('id')
        sp = Warehouse.objects.get(pk=id)
        sp.status =  not sp.status
        sp.save()
        data = {
            'message': sp.status
        }
        return redirect('deliver:warehouse')
    if request.GET.get('action') == 'reqdelete':
        id = request.GET.get('id')
        sp = Request.objects.get(pk=id)
        sp.status = False
        sp.save()
        data = {
            'message': sp.status
        }
        return redirect('deliver:requests')
    if request.method == 'POST':
        if request.POST.get('action') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('deliver:home')
        if request.POST.get('action') == 'add_cat':
            cat = Cat()
            cat.war_id = request.POST.get('war')
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
            cat.war_id = request.POST.get('war')
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
            cat = Cat.objects.get(id=int(request.POST.get('catId')))
            food.warehouse = cat.war
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
        if request.POST.get('action') == 'add_motor':
            dp = Motors()
            dp.title = request.POST.get('title')
            dp.number = request.POST.get('number')
            dp.image = request.FILES['images']
            dp.status =  request.FILES['status']
            dp.save()
            data = {
                'redirect': '/motors/',
                'message': 'success'
            }
        if request.POST.get('action') == 'deliver_add':
            dp = Dliver()
            dp.name = request.POST.get('name')
            dp.user_id = request.POST.get('user')
            dp.motor_id = request.POST.get('motor')
            dp.phone = request.POST.get('phone')
            dp.phoneId = request.POST.get('phoneId')
            dp.image = request.FILES['images']
            dp.save()
            data = {
                'redirect': '/delivers/',
                'message': 'success'
            }
        if request.POST.get('action') == 'warehouse':
            dp = Warehouse()
            dp.title = request.POST.get('title')
            dp.status = False
            dp.save()
            data = {
                'redirect': '/warehouse/',
                'message': 'success'
            }
        if request.POST.get('action') == 'deliver_edit':
            id = request.POST.get('id')
            dp = Dliver.objects.get(pk=id)
            dp.name = request.POST.get('name')
            dp.user_id = request.POST.get('user')
            dp.motor_id = request.POST.get('motor')
            dp.phone = request.POST.get('phone')
            dp.phoneId = request.POST.get('phoneId')
            image = request.FILES.get('images', False)
            if image:
                dp.image = request.FILES['images']
            dp.save()
            data = {
                'redirect': '/delivers/',
                'message': 'success'
            }
        if request.POST.get('action') == 'add_trasnport':
            dp = Transport()
            dp.dliver_id = request.POST.get('dliver')
            dp.request_id = request.POST.get('request')
            dp.start_date = datetime.datetime.now()
            dp.end_date = datetime.datetime.now()
            dp.save()
            id = request.POST.get('request')
            form = Request.objects.get(pk=id)
            form.status = True
            form.save()
            data = {
                'redirect': '/requests/',
                'message': 'success'
            }
        if request.POST.get('action') == 'motorEdit':
            id = request.POST.get('id')
            dp = Motors.objects.get(pk=id)
            dp.title = request.POST.get('title')
            dp.number = request.POST.get('number')
            image = request.FILES.get('images', False)
            if image:
                dp.image = request.FILES['images']
            status = request.FILES.get('status', False)
            if status:
                dp.status = True
            else:
                dp.status = False
            dp.save()
            data = {
                'redirect': '/motors/',
                'message': 'success'
            }
        if request.POST.get('action') == 'add_UsrBnka':
            print("awd")
            dp = BnkaUser()
            dp.bnka_id = request.POST.get('bnka')
            dp.user_id = request.POST.get('usrid')
            dp.save()
            data = {
                'redirect': '/accounts/',
                'message': 'success'
            }
        if request.POST.get('action') == 'add_user':
            post = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
                'password_repeat': request.POST.get('password_repeat'),
                'email': request.POST.get('email'),
            }
            form = UserForm(post)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                form.clean()
                form.save(commit=True)
                data = {
                    'redirect': '/accounts/',
                    'message': 'success'
                }
            else:
                errors = ''
                if form.errors:
                    for key, value in form.errors.items():
                        for error in value:
                            errors = error
                data = {
                    'message': errors
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

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializer.CustomerSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = serializer.RateSerializer

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motors.objects.all()
    serializer_class = serializer.MotorSerializer
