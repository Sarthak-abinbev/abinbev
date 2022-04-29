# todo/todo/urls.py : Main urls.py
'''
from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(todo_urls)),
]

from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]
'''


from django.urls import path
from accounts.views import MyObtainTokenPairView, RegisterView,LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
CountryMasterListApiView,BusinessFuncMasterListApiView, RoleMasterListApiView , Measuremasterlistapiview,Marketmasterlistapiview , 
Operatormasterlistapiview , Scopemasterlistapiview , Valuefiltermasterlistapiview,Prgranularitymasterlistapiview,Spacialgrmasterlistapiview
)



'''
from django.urls import path
from accounts.views import RegisterView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
'''
urlpatterns = [
    path('country/', CountryMasterListApiView.as_view()),
    path('businessFunction/', BusinessFuncMasterListApiView.as_view()),
    path('role/', RoleMasterListApiView.as_view()),
    path('market/', Marketmasterlistapiview.as_view()),
    path('measure/', Measuremasterlistapiview.as_view()),
    path('operator/', Operatormasterlistapiview.as_view()),
    path('scope/', Scopemasterlistapiview.as_view()),
    path('value/', Valuefiltermasterlistapiview.as_view()),
    path('product/', Prgranularitymasterlistapiview.as_view()),
    path('spacial/', Spacialgrmasterlistapiview.as_view())

]