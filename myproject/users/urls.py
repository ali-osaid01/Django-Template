from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, LogoutView, UserProfileView,UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

v1_urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]

v2_urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
]

urlpatterns = [
    path('v1/', include((v1_urlpatterns, 'v1'), namespace='v1')),
    path('v2/', include((v2_urlpatterns, 'v2'), namespace='v2')),   
] 