from django.contrib import admin

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog


@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    """Admin configuration for the InternshipPlacement model."""
    list_display = ("student", "company_name", "start_date", "end_date", "status")
    list_filter = ("status",)
    search_fields = ("student__username", "company_name")
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
    list_display = ("name", "weight", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    """Admin configuration for the Evaluation model."""
    list_display = ("weekly_log", "evaluator", "final_score", "created_at")
    search_fields = ("evaluator__username",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "final_score")
