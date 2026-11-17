from django.urls import path

from accounts.views import TrainerRegisterView,StudentRegisterView

urlpatterns = [
    
    path('register/trainer/',TrainerRegisterView.as_view()),
    
    path('register/student/',StudentRegisterView.as_view()),
]
