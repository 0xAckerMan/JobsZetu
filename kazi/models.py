from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.forms import ValidationError



# Create your models here.
class JobCategory(models.Model):
    job_categories = [
        ('Accounting and Finance', 'Accounting and Finance'),
        ('Administration and Office Support', 'Administration and Office Support'),                  
        ('Architecture and Engineering', 'Architecture and Engineering'),                  
        ('Arts and Design', 'Arts and Design'),                  
        ('Business and Management', 'Business and Management'),                  
        ('Construction and Trades', 'Construction and Trades'), ('Customer Service', 'Customer Service'),                  
        ('Education and Training', 'Education and Training'), ('Healthcare and Medical', 'Healthcare and Medical'),                  
        ('Hospitality and Tourism', 'Hospitality and Tourism'), ('Human Resources', 'Human Resources'),                  
        ('Information Technology', 'Information Technology'),                  
        ('Legal', 'Legal'),('Marketing and Communications', 'Marketing and Communications'),                  
        ('Non-profit and Volunteer', 'Non-profit and Volunteer'),('Retail and Sales', 'Retail and Sales'),                  
        ('Science and Technology', 'Science and Technology'),('Social Services', 'Social Services'),                  
        ('Transportation and Logistics', 'Transportation and Logistics'),
        ('other','other')
    ]

    job_subcategories = [
        ('Accounting and Finance', 'Financial analysis'), ('Accounting and Finance', 'Audit and taxation'),
        ('Accounting and Finance', 'Accounts payable/receivable'),                     
        ('Administration and Office Support', 'Executive assistance'),('Administration and Office Support', 'Office management'),
        ('Administration and Office Support', 'Reception and switchboard'),                     
        ('Architecture and Engineering', 'Civil engineering'),('Architecture and Engineering', 'Mechanical engineering'), 
        ('Architecture and Engineering', 'Electrical engineering'),         
        ('Arts and Design', 'Graphic design'),('Arts and Design', 'Photography'),('Arts and Design', 'Art direction'),                     
        ('Business and Management', 'Sales and marketing management'),('Business and Management', 'Operations management'),
        ('Business and Management', 'Project management'),                     
        ('Construction and Trades', 'Plumbing'),('Construction and Trades', 'Electrical'),('Construction and Trades', 'Carpentry'), 
        ('Customer Service', 'Call center'),('Customer Service', 'Helpdesk support'),('Customer Service', 'Technical support'),   
        ('Education and Training', 'Teaching and lecturing'),('Education and Training', 'Curriculum development'),
        ('Education and Training', 'Training and development'),
        ('Healthcare and Medical', 'Nursing'),('Healthcare and Medical', 'Pharmacy'), 
        ('Healthcare and Medical', 'Medical laboratory'),
        ('Hospitality and Tourism', 'Hotel and restaurant management'),('Hospitality and Tourism', 'Tourism and travel'),                     
        ('Hospitality and Tourism', 'Food and beverage service'),                    
        ('Human Resources', 'Recruitment and talent acquisition'),('Human Resources', 'Employee relations'),                     
        ('Human Resources', 'Compensation and benefits'),                    
        ('Information Technology', 'Software development'),('Information Technology', 'Network engineering'),
        ('Information Technology', 'Cybersecurity'),                     
        ('Legal', 'Corporate law'),('Legal', 'Litigation'),('Legal', 'Intellectual property'),
        ('Marketing and Communications', 'Public relations'),('Marketing and Communications', 'Brand management'),
        ('Marketing and Communications', 'Digital marketing'),                     
        ('Non-profit and Volunteer', 'Fundraising and development'),('Non-profit and Volunteer', 'Community outreach'),                     
        ('Non-profit and Volunteer', 'Volunteer management'),                     
        ('Retail and Sales', 'Retail management'),('Retail and Sales', 'Sales representative'),('Retail and Sales', 'Merchandising'),
        ('Science and Technology', 'Research and development'),('Science and Technology', 'Data analysis'),
        ('Science and Technology', 'Biotechnology'),
        ('Social Services', 'Social work'),('Social Services', 'Counseling'),('Social Services', 'Case management'),
        ('Transportation and Logistics', 'Truck driving'),('Transportation and Logistics', 'Supply chain management'),
        ('Transportation and Logistics', 'Warehouse operations'),
        ('other','other')
    ]

    subcategory_twice = [(sub[1], sub[1]) for sub in job_subcategories]
    
    job_category = models.CharField(max_length=50, choices=job_categories, default="other")
    other_job_category = models.CharField(max_length=100, blank=True, null=True)
    job_subcategory = models.CharField(max_length=50, choices=subcategory_twice, default="other")
    other_job_subcategory = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        if self.job_category == 'other' and not self.other_job_category:
            raise ValidationError('Please enter other Job Category name.')
        elif self.job_category  != "other" and str(self.other_job_category) != 'None':
            print(str(self.other_job_category))
            raise ValidationError('You have already provided a job category. Other Job Category name should be left blank.')
        

        if self.job_subcategory == 'other' and not self.other_job_subcategory:
            raise ValidationError('Please enter other Job Subcategory name.')
        elif self.job_subcategory  != "other" and str(self.other_job_subcategory) != "None":
            raise ValidationError('You have already provided a job subcategory. Other Job Subcategory name should be left blank.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
            myFields = []
            if self.job_category != "other":
                myFields.append(self.job_category)
            else:
                myFields.append(self.other_job_category)
            if self.job_subcategory != "other" :
                myFields.append(self.job_subcategory)
            else:
                myFields.append(self.other_job_subcategory)
            return f"{myFields[0]}  --  {myFields[1]}"
            

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
    rate_per_hour = models.CharField(max_length=30, null=True)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
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
    rate_per_hour = models.CharField(max_length=30, null=True)
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



