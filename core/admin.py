from django.contrib import admin
from .models import (
    Hero,
    About,
    Skill,
    TimelineEvent,
    Project,
    SocialLink,
    CV,
)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "title")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency")


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ("year", "title")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "tech_stack")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")
