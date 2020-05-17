# from django import forms
# from django.contrib import admin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Group
# from deliver.models import Account, Cat, Dliver, Food, Request, RequestDetail, Specify, Transport
# from django.utils.html import format_html

# # Register your models here.
# class CatAdmin(admin.ModelAdmin):
#     def image_tag(self, obj):
#         return format_html('<img src="{}" style="height: 50px;" />'.format(obj.image.url))

#     image_tag.short_description = 'وێنه‌'

#     list_display = ('nameEg','nameKu','detiles','image_tag')
#     fields = ( 'image', 'nameEg','nameKu','detiles',)
#     labels = {
#             'nameEg': 'ناوی به‌ ئینگللیزی',
#         }
#     readonly_fields = ["image_tag"]

# admin.site.register(Cat, CatAdmin)



# # Register your models here.
# class FoodAdmin(admin.ModelAdmin):
#     # inlines = [SpecifyInlines]
#     def image_tag(self, obj):
#         return format_html('<img src="{}" style="height: 50px;" />'.format(obj.image.url))
#     image_tag.short_description = 'وێنه‌'
#     fieldsets = (
#         ("زانیاری سه‌ره‌كی", {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ('image', 'title', 'price','category',),
#         }),
#         ("داشكاندن", {
           
#             'fields': ('disprice',),
#         }),
#         ('ورده‌كاری', {
#             'classes': ('collapse',),
#             'fields': ('subtitle', 'detiles'),
#         }),
#     )
#     list_display = ('title', 'image_tag', 'price', 'disprice','category','subtitle','detiles')
#     list_editable = ('category',)
#     search_fields = ('title','subtitle')

# class SpecifyInline(admin.TabularInline):

#     model = RequestDetail.specify.through
#     verbose_name = u"Specify"
#     verbose_name_plural = u"Specify"

# # Register your models here.
# class RequestDetailAdmin(admin.ModelAdmin):
#     list_display = ('food', 'quantity')

# # Register your models here.
# class RequestAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'address')

# admin.site.register(Food, FoodAdmin)

# # admin.site.register(Account)

# admin.site.register(Specify)

# admin.site.register(RequestDetail, RequestDetailAdmin)

# admin.site.register(Request, RequestAdmin)

# admin.site.register(Dliver)

# admin.site.register(Transport)


# ###customuser

# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = Account
#         fields = ('email', 'username')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Account
#         fields = ('email', 'password', 'username', 'is_active', 'is_admin','is_superuser')

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'username','is_active', 'is_admin','is_staff','is_superuser')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('زانیاری كه‌سی', {'fields': ('username',)}),
#         ('ریگه‌پیدان', {'fields': ('is_admin','is_active','is_staff','is_superuser')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2','is_staff', 'is_admin','is_superuser'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

# admin.site.register(Account, UserAdmin)
