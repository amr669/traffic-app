from . import views
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',views.index,name='index'),
    path('mycars' , views.profile, name='profile'),
    path('test/new/',views.new_carTest,name='new_car2'),
    path('payment/<int:v_n>/new',views.new_payment,name='new_pymnt'),
    path('p/<int:v_n1>',views.pay_done,name='pay_done'),
    path("click",views.click, name="click"),
    path("clic",views.clic, name="click1"),
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
    path('account/',views.UserUpdateView.as_view(),name='my_account')
]
