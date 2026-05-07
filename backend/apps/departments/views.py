from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Department
from .serializers import DepartmentSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'admin'

class DepartmentViewSet(viewsets.ModelViewSet):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	permission_classes = [IsAdminOrReadOnly]
