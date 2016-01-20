from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.forms import ModelForm

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



LEVEL_CHOICES = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5'),
    ('NO', 'NO'),
)
class ExamInfo(models.Model):
    name = models.CharField(max_length=10)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)


#---------------------------Uploading of files
class User(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to = './upload/')

    def __unicode__(self):
        return self.username


#---------------------------Programming the Django application
from django.db import models

class Input(models.Model):
    r = models.FloatField()



import wtforms as wtf

class Average(wtf.Form):
    filename   = wtf.FileField(validators=
                               [wtf.validators.InputRequired()])
