from django.contrib import admin
from .models import Candidate, JobList, Company, JobCategory, Education, WorkExperience

# Register your models here.

admin.site.register(Candidate)
admin.site.register(JobList)
admin.site.register(Company)
admin.site.register(Education)
admin.site.register(JobCategory)
admin.site.register(WorkExperience)
