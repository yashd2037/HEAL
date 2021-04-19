# Generated by Django 3.1.6 on 2021-04-16 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HEALSurvey', '0013_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCodeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('median_household_income', models.CharField(max_length=30)),
                ('two_bedroom_housing_wage', models.CharField(max_length=30)),
                ('estimated_prevalence_of_diabetes_in_adults', models.CharField(max_length=30)),
                ('healthy_food_access', models.CharField(max_length=30)),
                ('adult_asthma_rates', models.CharField(max_length=30)),
                ('high_blood_pressure', models.CharField(max_length=30)),
                ('heart_disease', models.CharField(max_length=30)),
                ('mental_health', models.CharField(max_length=30)),
                ('physical_health', models.CharField(max_length=30)),
                ('stroke', models.CharField(max_length=30)),
                ('lack_of_health_insurance', models.CharField(max_length=30)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HEALSurvey.city')),
                ('zipcode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HEALSurvey.zipcode')),
            ],
        ),
    ]