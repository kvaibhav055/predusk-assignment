from rest_framework import serializers
from .models import Profile, Skill, Project, WorkExperience


class SkillSerializer(serializers.ModelSerializer):
class Meta:
model = Skill
fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
skills = SkillSerializer(many=True, read_only=True)
class Meta:
model = Project
fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
class Meta:
model = WorkExperience
fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
skills = SkillSerializer(many=True, read_only=True)
projects = ProjectSerializer(many=True, read_only=True)
work = WorkExperienceSerializer(many=True, read_only=True)


class Meta:
model = Profile
fields = "__all__"
