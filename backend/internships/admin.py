from django.contrib import admin

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog

@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    """Admin configuration for the IntershipPlacement model."""

    # Columns displayed in the placement list view
    list_display = ("student", "company_name", "position_title", "start_date", "end_date", "status")

    # Filters available in the right sidebar
    last_filter = ("status",)
    
    # Fields that can be searched in the admin search bar
    search_field = ("student__username", "company_name", "position_title")

    # Order placements by most recent start date first
    ordering = ("-start_date",)

@admin.register(WeeklyLog)
class WeeklyLogAdmin(admin.ModelAdmin):
    """Admin configuration for the WeeklyLog model."""

    list_display = ("student", "week_number", "title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("student__username", "title")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    """Admin configuration for the EvaluationCriteria model."""

    list_display = ("name", "max_score")
    search_fields = ("name",)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    """Admin configuraton for the Evaluation model."""

    list_display = ("placement", "evaluator", "total_score", "created_at")
    search_fields = ("placement__company_name", "evaluator__username")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
