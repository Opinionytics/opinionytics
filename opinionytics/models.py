from django.db import models


class Popularity(models.Model):
    concept = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    score = models.IntegerField()


class Polarity(models.Model):
    polarity = models.CharField(max_length=50)
    confidence = models.DecimalField(max_digits=2, decimal_places=1)


class Topics(models.Model):
    topics = models.CharField(max_length=50)
    confidence = models.DecimalField(max_digits=2, decimal_places=1)


class Subjectivity(models.Model):
    subjectivity = models.CharField(max_length=50)
    confidence = models.DecimalField(max_digits=2, decimal_places=1)
