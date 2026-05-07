from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    # student is read-only because we set it automatically in the ViewSet
    student = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

    def validate_category(self, value):
        """Ensure the category matches the lowercase keys in models.py"""
        return value.lower()