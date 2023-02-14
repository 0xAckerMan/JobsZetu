from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profession_title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='candidate_photos/', null=True)
    video = models.FileField(upload_to='candidate_videos/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='candidate_featured_images/', blank=True, null=True)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE, default='default_category', null=True)
    skills = models.TextField(null=True)
    rate_per_hour = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    education_level = models.CharField(max_length=100, null=True)
    education_history = models.TextField(null=True)
    working_experience = models.TextField(null=True)
    resume = models.FileField(upload_to='candidate_resumes/', null=True)
    short_description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name
'''

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.ManyToManyField('Education', blank=True)
    work_experience = models.ManyToManyField('WorkExperience', blank=True)

    
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    
    def __str__(self):
        return self.name
'''

class JobList(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Remote', 'Remote'),
    )
    job_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    tag = models.CharField(max_length=100)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE)
    description = models.TextField()
    rate_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Archived', 'Archived'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    tagline = models.CharField(max_length=200)
    video = models.FileField(upload_to='company_videos/', blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/')
    email = models.EmailField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    team_size = models.PositiveIntegerField()
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE)
    description = models.TextField()
    date_started = models.DateField()
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



class JobCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Employer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    job_listings = models.ManyToManyField('JobList')
    
    def __str__(self):
        return self.name




class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="educations")
    school_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.school_name} ({self.candidate.name})'

class WorkExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.company_name} ({self.candidate.name})'
