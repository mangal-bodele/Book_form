from django.urls import path
from .views import user_login,user_logout,user_signup,pass_change

urlpatterns  = [
    path('singup/',user_signup,name='signup_url'),
    path('login/',user_login,name='login_url'),
    path('logout/',user_logout,name='logout_url'),
    path('change/',pass_change,name='change_url'),
]