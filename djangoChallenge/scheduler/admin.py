from sched import scheduler
from django.contrib import admin
from scheduler.models import Scheduler, Individual


# Register your models here.
@admin.register(Scheduler)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Request', 'status', 'date_to_execute')
    list_filter = ('status', 'Request')
    fields = ['title', 'Request', 'request_body', 'date_to_execute']

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'job_title')