from django.urls import path ,re_path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView



app_name= 'accounts'

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',CustomRegisterView.as_view(),name='register'),
    path('forget-password/',forget_password,name='forget-password'),
    # path('reset-password/',reset_password,name='reset-password'),
    # path('change-password/',change_password,name='change-password'),
    # path('change-password/',ChangePasswordView.as_view(),name='change-password'),
    path('reset-password/' , ResetPasswordView.as_view(),name = 'reset-password'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       CustomPaswordResetConfirmView.as_view() , name='password_reset_confirm'),
]
   

