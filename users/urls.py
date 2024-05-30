from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.user_logout, name='user_logout'),
]

#    path('login/', views.login, name='login'),
 #   path('registration/', views.registration, name='registration'),
  #  path('profile/', views.profile, name='profile'),
   # path('users-cart/', views.users_cart, name='users_cart'),
    #path('logout/', views.logout, name='logout'),