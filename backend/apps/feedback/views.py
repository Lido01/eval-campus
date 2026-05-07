from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .models import Feedback
from .serializers import FeedbackSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class IsAdminOrTargetedStaffOrOwner(permissions.BasePermission):
    """
    1. Admins have full access.
    2. Staff (Department/Student Affairs) can only view/update feedback targeted to them.
    3. Students can only view/update/delete their own feedback.
    """

    def has_permission(self, request, view):
        # This must return True for any logged-in user to reach the POST method
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        # Admin always has full access
        if user.role == 'admin':
            return True

        # Staff can only access if they are the designated 'target'
        if user.role in ['department', 'student_affairs']:
            return obj.target == user.role

        # Students can only access their own submissions
        return obj.student == user


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = [IsAdminOrTargetedStaffOrOwner]

    def get_queryset(self):
        """
        Filters the visibility of feedbacks based on user roles.
        """
        user = self.request.user
        if not user.is_authenticated:
            return Feedback.objects.none()

        # Admins see everything
        if user.role == 'admin':
            return Feedback.objects.all()

        # Staff see feedback targeted at their specific role
        if user.role in ['department', 'student_affairs']:
            return Feedback.objects.filter(target=user.role)

        # Students see only the feedback they personally created
        return Feedback.objects.filter(student=user)

    def perform_create(self, serializer):
        """
        Handles student ownership and anonymous flagging.
        Also creates a notification for the target user(s).
        """
        from apps.notifications.models import Notification
        from django.contrib.auth import get_user_model

        anonymous = self.request.data.get('anonymous', False)
        if isinstance(anonymous, str):
            anonymous = anonymous.lower() == 'true'

        if anonymous:
            feedback = serializer.save(student=None, anonymous=True)
        else:
            feedback = serializer.save(student=self.request.user, anonymous=False)

        # Notify the target user(s)
        User = get_user_model()
        target_users = User.objects.filter(role=feedback.target)
        for user in target_users:
            Notification.objects.create(
                user=user,
                message=f"New feedback submitted: {feedback.subject}"
            )

    def update(self, request, *args, **kwargs):
        """
        Restricts status updates to the targeted role or admins.
        """
        user = request.user
        instance = self.get_object()
        data = request.data.copy()

        # Check if user is trying to change the status
        if 'status' in data:
            # Check if user is the correct staff role or an admin
            is_targeted_staff = (user.role == instance.target)
            is_admin = (user.role == 'admin')

            if not (is_targeted_staff or is_admin):
                return Response(
                    {'detail': f'Only {instance.target} or Admin can change the status.'}, 
                    status=status.HTTP_403_FORBIDDEN
                )

        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        """Return the valid category choices from the model."""
        from .models import Feedback
        field = Feedback._meta.get_field('category')
        choices = [c[0] for c in getattr(field, 'choices', [])]
        return Response(choices)

    # --- Standard methods use super() but inherit the new logic above ---

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)