from django.urls import path
from deliver.api.views import(
	registration_view,
	ObtainAuthTokenView,
	account_properties_view,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "deliver"

urlpatterns = [
    path('login', ObtainAuthTokenView.as_view(), name="login"), 
    path('registar', registration_view, name="register")
]