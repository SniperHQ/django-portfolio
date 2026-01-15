from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


# =========================
# HERO
# =========================
class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    image = CloudinaryField("hero_image", blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# ABOUT
# =========================
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField("about_image", blank=True, null=True)

    def __str__(self):
        return self.title


# =========================
# SKILLS
# =========================
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    icon = CloudinaryField("skill_icon", blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# TIMELINE
# =========================
class TimelineEvent(models.Model):
    year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = CloudinaryField("timeline_icon", blank=True, null=True)

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
    image = CloudinaryField("project_image", blank=True, null=True)
    tech_stack = models.CharField(max_length=300)
    features = models.TextField(blank=True)
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
# SOCIAL LINKS
# =========================
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.TextField(blank=True)

    def __str__(self):
        return self.name


# =========================
# CV (PDF)
# =========================


class CV(models.Model):
    title = models.CharField(max_length=100, default="My CV")
    file = CloudinaryField(
        resource_type="image",  
        folder="cv"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
