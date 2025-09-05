import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "me_api_backend.settings")
django.setup()


from profiles.models import Profile, Skill, Project, WorkExperience


p, _ = Profile.objects.get_or_create(
email="you@example.com",
defaults={
"name": "Your Name",
"education": [{"school": "Your College", "degree": "B.Tech CSE", "start": "2021", "end": "2025"}],
"links": {"github": "https://github.com/yourid", "linkedin": "https://linkedin.com/in/yourid"}
}
)


s1, _ = Skill.objects.get_or_create(name="python", level=7)
s2, _ = Skill.objects.get_or_create(name="django", level=8)


p.skills.add(s1, s2)


proj = Project.objects.create(
title="SDN IDS Project",
description="Hybrid signature+anomaly IDS for SDN",
repo_url="https://github.com/yourid/sdn-ids",
profile=p
)
proj.skills.add(s1, s2)


WorkExperience.objects.get_or_create(
company="Predusk Technology",
role="Backend Intern",
start_date="2024-06-01",
profile=p,
description="Built APIs and optimized queries"
)


print("Seed done")
