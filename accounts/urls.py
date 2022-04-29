
from django.urls import path
from accounts.views import MyObtainTokenPairView, RegisterView,LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView

'''
from django.urls import path
from accounts.views import RegisterView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
'''
urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]
