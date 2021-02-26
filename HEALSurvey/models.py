from django.db import models


TOPIC_CHOICES = (
    ('Healthcare', 'Healthcare'),
    ('Transportation', 'Transportation'),
    ('Healthy Food', 'Healthy Food'),
    ('Housing', 'Housing'),
    ('Employment', 'Employment')
)

Yes_No_Question = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

Familiar_Question = (
    ('Not at all', 'Not at all'),
    ('Somewhat', 'Somewhat'),
    ('Familiar', 'Familiar'),
    ('Very familiar', 'Very familiar')
)

Agree_Question = (
    ('Strongly disagree', 'Strongly disagree'),
    ('Disagree', 'Disagree'),
    ('Agree', 'Agree'),
    ('Strongly Agree', 'Strongly Agree')
)


class Topics(models.Model):
    topic = models.CharField("First Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)
    topic2 = models.CharField("Second Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)

    def __str__(self):
        return self.topic


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # allows many choices to be assigned to a question
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
