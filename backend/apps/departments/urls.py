from django.urls import path
from .views import DepartmentViewSet

department_list = DepartmentViewSet.as_view({
	'get': 'list',
	'post': 'create',
})
department_detail = DepartmentViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
})

urlpatterns = [
	path('departments/', department_list, name='department-list'),
	path('departments/<int:pk>/', department_detail, name='department-detail'),
]
