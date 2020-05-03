from django.contrib import admin
from .models import Worker, WorkOrder
from .forms import WorkOrderForm

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'company')
    search_fields = ('name', 'email', 'company')
    ordering = ('id',)

@admin.register(WorkOrder)
class WorkerOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'deadline')
    search_fields = ('title', 'deadline')
    ordering = ('id',)
    form = WorkOrderForm