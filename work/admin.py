from django.contrib import admin

# Register your models here.

from .models import User, Project, WorkDivision, Work

admin.site.register(User)
admin.site.register(Project)
admin.site.register(WorkDivision)
admin.site.register(Work)
