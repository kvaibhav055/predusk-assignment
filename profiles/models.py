from django.db import models


class Profile(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  education = models.JSONField(null=True, blank=True)
  links = models.JSONField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
  name = models.CharField(max_length=100)
  level = models.IntegerField(default=1)
  profiles = models.ManyToManyField(Profile, related_name="skills")


class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  repo_url = models.URLField(null=True, blank=True)
  demo_url = models.URLField(null=True, blank=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
  skills = models.ManyToManyField(Skill, related_name="projects")
  created_at = models.DateTimeField(auto_now_add=True)


class WorkExperience(models.Model):
  company = models.CharField(max_length=200)
  role = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="work")

def __str__(self):
        return self.name
