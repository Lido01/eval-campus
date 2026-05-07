from django.urls import path
from .views import RegisterView, UserListView
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('register/', RegisterView.as_view(), name='register'),
	path('login/', CustomTokenObtainPairView.as_view(), name='login'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 
 	path('users/', UserListView.as_view(), name='user-list'),
]
