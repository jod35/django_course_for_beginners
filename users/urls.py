from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=LoginForm
    ),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='log_out')
]