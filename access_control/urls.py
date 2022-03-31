from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterUserView

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name="get_token_auth"),
    path('register/', RegisterUserView.as_view(), name="register")
]