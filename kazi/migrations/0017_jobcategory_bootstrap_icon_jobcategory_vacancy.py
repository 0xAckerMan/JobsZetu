# Generated by Django 4.1.6 on 2023-03-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kazi', '0016_joblist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='bootstrap_icon',
            field=models.CharField(blank=True, default='fa-solid fa-paperclip"', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobcategory',
            name='vacancy',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]