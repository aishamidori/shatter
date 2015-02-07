from django.db import models

# Create your models here.

class Comment(models.Model):
    position = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=None, decimal_places=None)
    tag = models.CharField(max_length=15)
    company = models.ForeignKey('Company')
    def __str__(self):
        return self.comment

class Company(models.Model):
    name = models.CharField(max_length=50) 
    employees = models.FloatField()
    website = models.URLField()
    statistic = models.OnetoOneField('Statistic')
    diversity = models.DecimalField(max_digits=None, decimal_places=None)
    
    def __str__(self):
        return self.name

class Statistic(models.Model):
	diversity = models.DecimalField(max_length=4)
	inclusivity = models.DecimalField(max_length=4)




