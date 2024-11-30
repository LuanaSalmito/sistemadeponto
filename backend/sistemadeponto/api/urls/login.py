from django.urls import path
from api.views.login import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
