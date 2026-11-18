from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import TrainerRegisterView,StudentRegisterView
from accounts.views import TrainerProfileDetailView,TrainerProfileUpdateView


urlpatterns = [
    
    path('register/trainer/',TrainerRegisterView.as_view()),
    
    path('register/student/',StudentRegisterView.as_view()),
    
    path('token/',ObtainAuthToken.as_view()),
    
    path('trainerprofile/',TrainerProfileDetailView.as_view()),
    
    path('trainerprofile/edit/',TrainerProfileUpdateView.as_view()),
]
