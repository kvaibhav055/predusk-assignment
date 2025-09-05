from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile, Project, Skill, WorkExperience
from .serializers import ProfileSerializer, ProjectSerializer, SkillSerializer, WorkExperienceSerializer


class ProfileViewSet(viewsets.ModelViewSet):
queryset = Profile.objects.all()
serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
queryset = Project.objects.all()
serializer_class = ProjectSerializer
filter_backends = [filters.SearchFilter]
search_fields = ["title", "description", "skills__name"]


class SkillViewSet(viewsets.ModelViewSet):
queryset = Skill.objects.all()
serializer_class = SkillSerializer


class WorkViewSet(viewsets.ModelViewSet):
queryset = WorkExperience.objects.all()
serializer_class = WorkExperienceSerializer


@api_view(["GET"])
def health(request):
return Response({"status": "ok"})
