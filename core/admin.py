from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Hero,
    About,
    Skill,
    TimelineEvent,
    SocialLink,
    Project
)


# =========================
# HERO (Singleton enforced)
# =========================
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'github_url')
    search_fields = ('name', 'title')

    def has_add_permission(self, request):
        # Allow only one Hero record
        return not Hero.objects.exists()


# =========================
# ABOUT
# =========================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)
    fields = ('title', 'description', 'image', 'cv')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# =========================
# SKILLS
# =========================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'icon_preview')
    search_fields = ('name',)
    list_filter = ('proficiency',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<img src="{}" style="height:40px;" />',
                obj.icon.url
            )
        return "-"

    icon_preview.short_description = "Icon"


# =========================
# TIMELINE
# =========================
@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    search_fields = ('title',)
    ordering = ('year',)


# =========================
# PROJECTS
# =========================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image_preview')
    search_fields = ('title', 'tech_stack')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# =========================
# SOCIAL LINKS (SVG RENDER)
# =========================
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon_preview')
    search_fields = ('name', 'url')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<div style="width:30px;height:30px;">{}</div>',
                obj.icon
            )
        return "-"

    icon_preview.short_description = "Icon"
