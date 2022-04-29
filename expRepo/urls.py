
from django.urls import path
from accounts.views import RegisterView, LogoutView, LogoutAllView
from .views import ExperimentRepoView , TotalExperiment,TotalInProgressExperiment,TotalNotStartedExperiment,TotalCompletedExperiment
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('expRepo/', ExperimentRepoView.as_view()),
    path('expRepocount/', TotalExperiment.as_view()),
    path('expRIP/', TotalInProgressExperiment.as_view()),
    path('expRNS/', TotalNotStartedExperiment.as_view()),
    path('expRCompleted/', TotalCompletedExperiment.as_view()),
    ]
    