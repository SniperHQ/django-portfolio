from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# =========================
# HERO (Singleton Content)
# =========================
class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# ABOUT SECTION
# =========================
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.title


# =========================
# SKILLS
# =========================
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage (0–100)"
    )
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# TIMELINE
# =========================
class TimelineEvent(models.Model):
    year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='timeline/', blank=True, null=True)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return f"{self.year} - {self.title}"


# =========================
# PROJECTS
# =========================
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(
        max_length=300,
        help_text="Comma-separated values e.g. Django, PostgreSQL, JavaFX"
    )
    features = models.TextField(
        blank=True,
        help_text="One feature per line"
    )
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def feature_list(self):
        return self.features.splitlines()

    def __str__(self):
        return self.title


# =========================
# SOCIAL LINKS (SVG READY)
# =========================
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.TextField(
        blank=True,
        help_text="Paste SVG or HTML icon code"
    )

    def __str__(self):
        return self.name
