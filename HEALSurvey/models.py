from django.db import models


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
    ('Strongly disagree', 'Strongly disagree'),
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
