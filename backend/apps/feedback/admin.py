from django.contrib import admin

# Register your models here.
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'category', 'target', 'status', 'created_at')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('subject', 'description', 'student__username')