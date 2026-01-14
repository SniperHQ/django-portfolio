
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    tech_stack = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(max_length=500, blank=True, null=True)
    github_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        if self.tech_stack:
            return [tech.strip() for tech in self.tech_stack.split(',')]
        return []

    @property
    def feature_list(self):
        if self.features:
            return [feature.strip() for feature in self.features.split(',')]
        return []
