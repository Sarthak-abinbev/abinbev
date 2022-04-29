
from django.urls import path
from accounts.views import MyObtainTokenPairView, RegisterView,LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CountryMasterListApiView,BusinessFuncMasterListApiView, RoleMasterListApiView, ValueMasterListApiView, 
    ValueMasterListbyJsonApiView, ValueMasterListbyScopeApiView, ScopeMasterListApiView, MeasureMasterListApiView
)
#urlpatterns = [path('country/',CountryMasterListApiView.as_view())]
# path('country/',CountryMasterListApiView.as_view()),
urlpatterns = [
    path('country/',CountryMasterListApiView.as_view()),
    path('businessFunction/',BusinessFuncMasterListApiView.as_view()),
    path('role/',RoleMasterListApiView.as_view()),
    path('scopeFilterValue/<int:id>',ValueMasterListApiView.as_view()),
    path('scopeFilterValueByScope/<str:id>',ValueMasterListbyScopeApiView.as_view()),
    path('valueFilterOperations/',ValueMasterListbyJsonApiView.as_view()),
    path('scopeFilter/<int:id>',ScopeMasterListApiView.as_view()),
    path('marketMaster/<int:marketMasterId>',MeasureMasterListApiView.as_view())
]


