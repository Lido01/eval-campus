from django.urls import path
from .views import FeedbackViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

feedback_list = FeedbackViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
feedback_detail = FeedbackViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
feedback_categories = FeedbackViewSet.as_view({
    'get': 'categories',
})

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('feedbacks/', feedback_list, name='feedback-list'),
    path('feedbacks/<int:pk>/', feedback_detail, name='feedback-detail'),
    path('feedbacks/categories/', feedback_categories, name='feedback-categories'),
]
