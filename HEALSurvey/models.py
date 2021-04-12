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

    def __str__(self):
        return self.summary_text_a


class UserChoices(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    u_choice = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.username)

# class SummaryChoice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    s_choice = models.CharField(max_length=1, blank=True)

#    def __str__(self):
#        return self.s_choice


# class Report(models.Model):
#     id = models.IntegerField(primary_key=True)
#    schoice = models.ForeignKey(SummaryChoices, on_delete=models.CASCADE)