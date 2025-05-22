from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)


v1_urlpatterns = [
   
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    
    path('', include(router.urls)),
]

urlpatterns = [
    path('v1/', include((v1_urlpatterns, 'v1'), namespace='v1')),
] 