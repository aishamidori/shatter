from django.db import models

# Create your models here.

class Comment(models.Model):
    position = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    rating = models.FloatField()
    tag = models.ForeignKey('Tag_Type', null=True)
    company = models.ForeignKey('Company', null=True)
    def __str__(self):
        return self.comment

class Company(models.Model):
    name = models.CharField(max_length=50) 
    website = models.URLField()
    statistic = models.OnetoOneField('Statistic')
    diversity = models.DecimalField(max_digits=None, decimal_places=None)
    def __str__(self):
        return self.name

class Statistic(models.Model):
	tag_type = models.ForeignKey('Tag_Type', null=True)
	count = models.IntegerField()

class Tag_Type(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
