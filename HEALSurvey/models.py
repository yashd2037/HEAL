from django.db import models
from django.contrib.auth.models import User

TOPIC_CHOICES = (
    ('Healthcare', 'Healthcare'),
    ('Transportation', 'Transportation'),
    ('Healthy Food', 'Healthy Food'),
    ('Housing', 'Housing'),
    ('Employment', 'Employment')
)

QUESTION_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('True', 'True'),
    ('False', 'False'),
    ('Strongly Disagree', 'Strongly Disagree'),
    ('Disagree', 'Disagree'),
    ('Agree', 'Agree'),
    ('Strongly Agree', 'Strongly Agree'),
    ('Not at all', 'Not at all'),
    ('Somewhat', 'Somewhat'),
    ('Familiar', 'Familiar'),
    ('Very familiar', 'Very familiar')

)


class Topics(models.Model):
    topic = models.CharField("First Topic", max_length=15, blank=True, null=True, choices=TOPIC_CHOICES)
    topic2 = models.CharField("Second Topic", max_length=15, blank=True, null=True, choices=TOPIC_CHOICES)

    def __str__(self):
        return self.topic


class Question(models.Model):
    QuestionText = models.CharField(max_length=600)
    InfoText = models.CharField(max_length=600, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    PreviousID = models.IntegerField(default=1)
    NextIDA = models.IntegerField(default=1)
    NextIDB = models.IntegerField(default=1)
    VideoLink = models.CharField(max_length=600, blank=True, null=True)
    WebsiteLink = models.CharField(max_length=600, blank=True, null=True)
    WebsiteLinkAlt = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.QuestionText


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # allows many choices to be assigned to a question
    choice_text = models.CharField(max_length=20, blank=True, choices=QUESTION_CHOICES)

    def __str__(self):
        return self.choice_text


class SummaryStatement(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    summary_text_a = models.CharField(max_length=500, blank=True)
    summary_text_b = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Summary Statement"
        verbose_name_plural = "Summary Statements"
    def __str__(self):
        return self.summary_text_a


class UserChoices(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    u_id = models.IntegerField(default=0)
    u_choice = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "User Choices"
    def __str__(self):
        return str(self.username)


class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class ZipCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Zip Code"
        verbose_name_plural = "Zip Codes"

    def __str__(self):
        return self.city.name + ' : ' + self.zipcode


class CityData(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    medianFamilyIncome = models.CharField(max_length=30)
    twoBedroomHousingWage = models.CharField(max_length=30)
    prevalenceDiabetesInAdults = models.CharField(max_length=30)
    walkScore = models.CharField(max_length=30)
    housingTransportationAffordability = models.CharField(max_length=30)
    healthyFoodAccess = models.CharField(max_length=30)
    asthmaRate = models.CharField(max_length=30)

    def __str__(self):
        return self.medianFamilyIncome


class ZipCodeData(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    median_household_income = models.CharField(max_length=30)
    two_bedroom_housing_wage = models.CharField(max_length=30)
    estimated_prevalence_of_diabetes_in_adults = models.CharField(max_length=30)
    healthy_food_access = models.CharField(max_length=30)
    adult_asthma_rates = models.CharField(max_length=30)
    high_blood_pressure = models.CharField(max_length=30)
    heart_disease = models.CharField(max_length=30)
    mental_health = models.CharField(max_length=30)
    physical_health = models.CharField(max_length=30)
    stroke = models.CharField(max_length=30)
    lack_of_health_insurance = models.CharField(max_length=30)

    class Meta:
        db_table = 'HEALSurvey_zipcodedata'
        verbose_name_plural = "Zip Code Data"

    def __str__(self):
        return self.city.name + ' : ' + self.zipcode.zipcode


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
