from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('', 'Unknown'),
)

TICKET_CLASS_CHOICES = (
    ('0', 'Unknown'),
    ('1', '1st Class'),
    ('2', '2nd Class'),
    ('3', '3rd Class'),
)

EMBARKED_PORT_CHOICES = (
    ('S', 'Southampton'),
    ('C', 'Cherbourg'),
    ('Q', 'Queenstown'),
    ('', 'Unknown')
)

class Passenger(models.Model):
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    survived = models.BooleanField(default=False)
    ticket_class = models.IntegerField(choices=TICKET_CLASS_CHOICES, blank=False, null=False, default=3)
    embarked = models.CharField(max_length=1, choices=EMBARKED_PORT_CHOICES, blank=True)
    age = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class ADR(models.Model):
    load = models.CharField(max_length=100, blank=True)
    cyl1 = models.FloatField(blank=True, null=True)
    cyl2 = models.FloatField(blank=True, null=True)
    cyl3 = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    cov  = models.FloatField(blank=True, null=True)
    rsr  = models.FloatField(blank=True, null=True)
    unknwn = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return self.load