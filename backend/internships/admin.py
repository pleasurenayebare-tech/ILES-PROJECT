from django.contrib import admin

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog

@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    """Admin configuration for the IntershipPlacement model."""

    # Columns displayed in the placement list view
    list_display = ("student", "company_name", "position_title", "start_date", "end_date", "status")

    # Filters available in the right sidebar
