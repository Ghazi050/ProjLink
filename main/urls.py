from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('developer-profile/', views.developer_profile_view, name='developer_profile'),
    path('owner-profile/', views.owner_profile_view, name='owner_profile'),
    path('social-auth-callback/', views.social_auth_callback, name='social_auth_callback'),
]
