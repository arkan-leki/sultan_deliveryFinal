from django.urls import path

from api.api.views import (
    registration_view,
    ObtainAuthTokenView,
)

app_name = "deliver"

urlpatterns = [
    path('login', ObtainAuthTokenView.as_view(), name="login"),
    path('registar', registration_view, name="register")
]
