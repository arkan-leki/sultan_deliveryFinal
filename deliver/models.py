from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_resized import ResizedImageField

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    class Meta:
        verbose_name_plural = "هه‌ژمار"


class Warehouse(models.Model):
    title = models.CharField(max_length=110)
    image = ResizedImageField(size=[300, 300], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name='وێنه‌')
    add_date = models.DateTimeField(verbose_name='add date', auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def items(self):
        items = self.Cat_warehouse.count
        return items

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "بنکە"


class Cat(models.Model):
    war = models.ForeignKey(
        Warehouse, related_name='Cat_warehouse', on_delete=models.CASCADE, default=1)
    image = ResizedImageField(size=[400, 400], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name='وێنه‌')
    nameEg = models.CharField(max_length=100, verbose_name="ناوی بیانی")
    nameKu = models.CharField(max_length=100, verbose_name="ناوی كوردی")
    deleted = models.BooleanField(default=False)
    date_added = models.DateField(
        verbose_name='ریكه‌وتی دانان', auto_now_add=True)

    def __str__(self):
        return self.nameEg

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "جۆره‌كانی خواردن"


class Food(models.Model):
    category = models.ForeignKey(
        Cat, related_name='Food_category', on_delete=models.CASCADE)
    image = ResizedImageField(size=[400, 400], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name="وێنه‌")
    sell_price = models.CharField(max_length=11, verbose_name="نرخ")
    title = models.CharField(max_length=50, verbose_name="ناو")
    subtitle = models.CharField(max_length=300, verbose_name="ناونیشان")
    detiles = models.CharField(max_length=300, verbose_name="ورده‌كاری")
    date_add = models.DateField(auto_now_add=True, verbose_name="به‌ره‌واری دانان")
    cost = models.CharField(max_length=11, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def popularity(self):
        likes = self.rate_food.count
        return likes

    def dispriceDate(self):
        try:
            queryset = self.disprice_food.get(exp_date__gt=datetime.now()).exp_date
            return queryset
        except ObjectDoesNotExist:
            return self.disprice_food.filter(exp_date__gt=datetime.now()).exists()

    def dispriceId(self):
        try:
            queryset = self.disprice_food.get(exp_date__gt=datetime.now()).id
            return queryset
        except ObjectDoesNotExist:
            return self.disprice_food.filter(exp_date__gt=datetime.now()).exists()

    def dispriceTitle(self):
        try:
            queryset = self.disprice_food.get(exp_date__gt=datetime.now()).title
            return queryset
        except ObjectDoesNotExist:
            return self.disprice_food.filter(exp_date__gt=datetime.now()).exists()

    def disprice(self):
        try:
            queryset = self.disprice_food.get(exp_date__gt=datetime.now()).price
            return queryset
        except ObjectDoesNotExist:
            return self.disprice_food.filter(exp_date__gt=datetime.now()).exists()

    def isDispriced(self):
        return self.disprice_food.filter(exp_date__gt=datetime.now()).exists()

    def __unicode__(self):
        return

    def avg_ratings(self):
        the_values = self.rate_food.aggregate(Avg('stars')).values()
        return list(the_values)[0]

    class Meta:
        verbose_name_plural = "خواردنه‌كان"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Specify(models.Model):
    food = models.ForeignKey(
        Food, related_name='specifies', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=11, verbose_name="نرخ")
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "تام و چێش"


class Dipricing(models.Model):
    food = models.ForeignKey(
        Food, related_name='disprice_food', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=11, verbose_name="نرخ")
    start_date = models.DateField(verbose_name='start added')
    exp_date = models.DateField(verbose_name='expire added')
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "disprice"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(max_length=100)
    instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    phoneid = models.CharField(max_length=110, default='Unknown')
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = ResizedImageField(size=[300, 300], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name="وێنه‌")

    def __str__(self):
        return self.name


class Favorate(models.Model):
    food = models.ForeignKey(Food, related_name='fav_food', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='fav_user', on_delete=models.CASCADE)


class Rate(models.Model):
    food = models.ForeignKey(Food, related_name='rate_food', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='rate_user', on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)


class Request(models.Model):
    customer = models.ForeignKey(Customer, related_name='relcustomer', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=110)
    phone = models.CharField(max_length=110)
    address = models.CharField(max_length=110)
    total_price = models.CharField(max_length=11)
    dashkandin = models.CharField(max_length=11, blank=True)
    request_detail = models.ManyToManyField('RequestDetail')
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)
    last_edit = models.DateTimeField(verbose_name='last edit', auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "داواكاریه‌كان"


class RequestDetail(models.Model):
    food = models.ForeignKey(
        Food, related_name='form_food', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=11)
    specify = models.ManyToManyField('Specify')
    total_price = models.CharField(max_length=11)
    dashkandin = models.CharField(max_length=11, blank=True)
    customer = models.ForeignKey(Customer, related_name='customerRequestD', on_delete=models.CASCADE, default=1)
    date_added = models.DateField(
        verbose_name='date added', auto_now_add=True)
    last_edit = models.DateTimeField(verbose_name='last edit', auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.food.title + str(self.total_price)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "ورده‌كاری داواكاری"


class Motors(models.Model):
    title = models.CharField(max_length=110, blank=True, null=True)
    number = models.CharField(max_length=11, blank=True, null=True)
    image = ResizedImageField(size=[300, 300], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name="وێنه‌")
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "Motors"


class Dliver(models.Model):
    name = models.CharField(max_length=110, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motors, related_name='owed_motor', on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, blank=True, null=True)
    phoneId = models.CharField(max_length=110, blank=True, null=True)
    image = ResizedImageField(size=[200, 200], quality=50,
        upload_to='images/', blank=True, null=True, verbose_name="وێنه‌")

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "شۆفێر"


class Transport(models.Model):
    dliver = models.ForeignKey(Dliver, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    start_date = models.DateTimeField(verbose_name='start date')
    end_date = models.DateTimeField(verbose_name='end date')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.request)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "باركراو"


class BnkaUser(models.Model):
    bnka = models.ForeignKey(
        Warehouse, related_name='BnkaUser', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='BnkasUser', on_delete=models.CASCADE)
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return str(self.bnka) + " " + str(self.user)

    def __unicode__(self):
        return

    class Meta:
        verbose_name_plural = "بنکەو بەکارهێنەر"
