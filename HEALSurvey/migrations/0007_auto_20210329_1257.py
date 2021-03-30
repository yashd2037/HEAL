# Generated by Django 3.1.6 on 2021-03-29 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HEALSurvey', '0006_auto_20210316_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('True', 'True'), ('False', 'False'), ('Strongly disagree', 'Strongly disagree'), ('Disagree', 'Disagree'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree'), ('Not at all', 'Not at all'), ('Somewhat', 'Somewhat'), ('Familiar', 'Familiar'), ('Very familiar', 'Very familiar')], max_length=20),
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
        migrations.CreateModel(
            name='SummaryChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_choice', models.CharField(blank=True, max_length=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HEALSurvey.question')),
            ],
        ),
    ]
