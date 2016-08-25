from django.contrib import admin

# Register your models here.

from .models import Project, WorkDivision, Work

admin.site.register(Project)
admin.site.register(WorkDivision)
admin.site.register(Work)
