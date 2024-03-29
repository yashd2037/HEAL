# Generated by Django 3.1.6 on 2021-03-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HEALSurvey', '0002_auto_20210226_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ImageLink',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='NextIDA',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='NextIDB',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='PreviousID',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='VideoLink',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='WebsiteLink',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
