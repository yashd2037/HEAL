from django.db import models


TOPIC_CHOICES = (
    ('Healthcare', 'Healthcare'),
    ('Transportation', 'Transportation'),
    ('Healthy Food', 'Healthy Food'),
    ('Housing', 'Housing'),
    ('Employment', 'Employment')
)

class Topics(models.Model):
    topic = models.CharField("First Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)
    topic2 = models.CharField("Second Topic", max_length=15, blank=True, choices=TOPIC_CHOICES)

    def __str__(self):
        return self.topic
