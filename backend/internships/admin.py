from django.contrib import admi

from .models import Evaluation, EvaluationCriteria, InternshipPlacement, WeeklyLog

admin.site.register(InternshipPlacement)
admin.site.register(WeeklyLog)
admin.site.register(EvaluationCriteria)
admin.site.register(Evaluation)
