from django.urls import path
from .views import NotificationViewSet
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

notification_list = NotificationViewSet.as_view({
	'get': 'list',
	'post': 'create',
})
notification_detail = NotificationViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
})

urlpatterns = [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('notifications/', notification_list, name='notification-list'),
	path('notifications/<int:pk>/', notification_detail, name='notification-detail'),
]
