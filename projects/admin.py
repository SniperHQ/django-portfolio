from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_url', 'github_url')
    search_fields = ('title',)
    list_filter = ('tech_stack',)

admin.site.register(Project, ProjectAdmin)