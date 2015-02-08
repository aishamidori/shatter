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
    image = models.ImageField(upload_to="test", default="static/images/hab.svg", blank=True)

    percent_women = models.FloatField(default=0.0)
    # statistic = models.OneToOneField('Statistic', null=True)#default= Statistic(diversity = 0.00, inclusivity = 0.00))
    # statistics = ForeignKey('')
	
    overall_rating = models.FloatField(default=0.0)
    diversity = models.FloatField(default=0.0)
    inclusivity = models.FloatField(default=0.0)

    # overall_diversity = through_fields('Tag_Type', models.IntegerField())
    # diversity = through_fields('Tag_Type', models.IntegerField())
    # inclusivity = through_fields('Tag_Type', models.IntegerField())
    

    def __str__(self):
        return self.name

#class Statistic(models.Model):
	#tag_type = models.ForeignKey('Tag_Type', null=True)
	#count = models.IntegerField()

class Tag_Type(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
