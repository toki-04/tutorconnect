# Generated by Django 5.0.7 on 2024-08-06 05:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_learnerprofile_email_tutorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnerprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
