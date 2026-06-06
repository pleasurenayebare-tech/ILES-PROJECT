from django.contrib import admin

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog

@admin.register(InternshipPlacement)
admin.site.register(WeeklyLog)
admin.site.register(EvaluationCriteria)
admin.site.register(Evaluation)
