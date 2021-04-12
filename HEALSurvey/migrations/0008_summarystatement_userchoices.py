# Generated by Django 3.1.6 on 2021-04-12 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HEALSurvey', '0007_auto_20210405_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('u_choice', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SummaryStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_text_a', models.CharField(blank=True, max_length=500)),
                ('summary_text_b', models.CharField(blank=True, max_length=500)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HEALSurvey.question')),
            ],
        ),
    ]
