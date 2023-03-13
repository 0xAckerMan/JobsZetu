from django.contrib import admin
from .models import Candidate, JobList, Company, JobCategory, BackgroundData, Employer

# Register your models here.

admin.site.register(Candidate)
admin.site.register(JobList)
admin.site.register(Company)
admin.site.register(JobCategory)
admin.site.register(BackgroundData)
admin.site.register(Employer)
