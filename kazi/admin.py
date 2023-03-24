from django.contrib import admin
from .models import Candidate, JobList, Company, JobCategory, BackgroundData, Employer
from django import forms

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    change_form_template = 'kazi/my_change_form.html'

    # list_display = ('job_category', 'other_job_category', 'job_subcategory','other_job_subcategory')

admin.site.register(JobCategory, JobAdmin)



admin.site.register(Candidate)
admin.site.register(JobList)
admin.site.register(Company)
# admin.site.register(JobCategory)
admin.site.register(BackgroundData)
admin.site.register(Employer)
