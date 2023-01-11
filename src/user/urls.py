from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import login_page, register_page, my_account, logout_view, password_reset_request, MyObtainTokenPairView, \
    RegisterView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    path('my-account/', my_account, name='my-account'),
    path("password_reset/", password_reset_request, name="password_reset"),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),

]
