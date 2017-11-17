from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    rating = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField('questions.Tag', blank=True)


class Answer(models.Model):
    description = models.CharField(max_length=600)
    rating = models.PositiveIntegerField(default=0)
    correctness = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question)


class Tag(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question)
