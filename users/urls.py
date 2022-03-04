from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='log_out')
]