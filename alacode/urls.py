from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

app_name = "alacode"

urlpatterns = [
    path('', views.CodingView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
