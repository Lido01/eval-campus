from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if hasattr(request.user, 'role') and request.user.role in ['admin', 'department', 'student_affairs']:
			return True
		return obj.user == request.user

class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer
	permission_classes = [IsOwnerOrAdminOrReadOnly]

	def get_queryset(self):
		user = self.request.user
		# Debug: print user info
		print(f"[NotificationViewSet] user: {user}, is_authenticated: {user.is_authenticated}, role: {getattr(user, 'role', None)}")
		if not user.is_authenticated:
			return Notification.objects.none()
		# Only admin sees all notifications; others see only their own
		if hasattr(user, 'role') and user.role == 'admin':
			return Notification.objects.all()
		return Notification.objects.filter(user=user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
from django.shortcuts import render

# Create your views here.
