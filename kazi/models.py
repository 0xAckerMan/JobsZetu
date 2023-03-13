from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Candidate(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profession_title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='candidate_photos/', null=True)
    video = models.FileField(upload_to='candidate_videos/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='candidate_featured_images/', blank=True, null=True)
    skills = models.TextField(null=True)
    rate_per_hour = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    Jobcategory = models.ForeignKey(JobCategory, on_delete=models.CASCADE, blank=True, null=True)
    resume = models.FileField(upload_to='candidate_resumes/', null=True)
    short_description = models.TextField(null=True)

    def __str__(self):
        return self.name


# signals 1

@receiver(post_save, sender=User)
def create_candidate(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.email, instance.username,"oooooooooopppppjjj")
        Candidate.objects.create(user=instance, email=instance.email, name=instance.username)
        print(instance, 'candidate created')


@receiver(post_save, sender=User)
def save_candidate(sender, instance, *args, **kwargs):
    instance.candidate.save()

class BackgroundData(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='work_experiences', null=True)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    work_start_date = models.DateField()
    work_end_date = models.DateField()
    institution= models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    institution_start_date = models.DateField()
    institution_end_date = models.DateField()

    def __str__(self):
        return f'{self.company_name})'



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
    image = models.ImageField(upload_to='media/job_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    tagline = models.CharField(max_length=200)
    video = models.FileField(upload_to='media/company_videos/', blank=True, null=True)
    logo = models.ImageField(upload_to='media/company_logos/')
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




class Employer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    job_listings = models.ManyToManyField('JobList')
    
    def __str__(self):
        return self.name



