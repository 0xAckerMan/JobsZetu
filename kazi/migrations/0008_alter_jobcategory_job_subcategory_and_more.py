# Generated by Django 4.1.5 on 2023-03-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kazi', '0007_alter_jobcategory_other_job_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcategory',
            name='job_subcategory',
            field=models.CharField(default='other', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='other_job_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='other_job_subcategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]