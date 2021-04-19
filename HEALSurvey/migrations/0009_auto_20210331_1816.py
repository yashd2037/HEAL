# Generated by Django 3.1.6 on 2021-03-31 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HEALSurvey', '0008_auto_20210331_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoices',
            name='Username',
        ),
        migrations.AddField(
            model_name='userchoices',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]