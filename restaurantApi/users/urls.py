from django.urls import path
from .views import SignUpView, CustomTokenObtainPairView, UserListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),  # only for admin
]