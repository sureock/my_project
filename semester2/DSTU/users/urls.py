# urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Профили
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile, name='profile'),
    
    # Список пользователей
    path('users/', views.users_list, name='users_list'),
    path('users/all/', views.all_users_list, name='all_users_list'),
    
    # Управление друзьями
    path('friend/add/<str:username>/', views.add_friend, name='add_friend'),
    path('friend/remove/<str:username>/', views.remove_friend, name='remove_friend'),
    path('admin/logs/', views.view_logs, name='view_logs'),
]