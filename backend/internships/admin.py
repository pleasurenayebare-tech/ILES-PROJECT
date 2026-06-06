from django.contrib import admin

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog

@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    """Admin configuration for the IntershipPlacement model."""

    # Columns displayed in the placement list view
