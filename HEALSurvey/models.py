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

Question_Types = (
    ('Yes_No_Question', 'Yes_No_Question'),
    ('Agree_Question', 'Agree_Question'),
    ('Familiar_Question', 'Familiar_Question')
)


class Topics(models.Model):
    topic = models.CharField("First Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)
    topic2 = models.CharField("Second Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)

    def __str__(self):
        return self.topic


class Question(models.Model):
    QuestionText = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    PreviousID = models.IntegerField(default=1)
    NextIDA = models.IntegerField(default=1)
    NextIDB = models.IntegerField(default=1)
    VideoLink = models.CharField(max_length=200, blank=True, null=True)
    ImageLink = models.CharField(max_length=200, blank=True, null=True)
    WebsiteLink = models.CharField(max_length=200, blank=True, null=True)
    # type = models.CharField(max_length=100, choices=Question_Types)

    def __str__(self):
        return self.QuestionText


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # allows many choices to be assigned to a question
    choice_text = models.CharField(max_length=200)
    # if Question.type == 'Yes_No_Question':
    #     for count in Yes_No_Question:
    #         choice_text = Yes_No_Question[count]
    # elif Question.type == 'Agree_Question':
    #     for count in Agree_Question:
    #         choice_text = Agree_Question[count]
    # elif Question.type == 'Familiar_Question':
    #     for count in Familiar_Question:
    #         choice_text = Familiar_Question[count]

    def __str__(self):
        return self.choice_text
