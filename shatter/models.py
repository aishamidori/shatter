from django.db import models

# Create your models here.

class Comment(models.Model):
    companyId = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    rating = models.CharField(max_length=2)
    tag = models.CharField(max_length=15)
    def __str__(self):
        return self.comment

class Company(models.Model):
    name = models.CharField(max_length=50) 
    uniqueId = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    employees = models.FloatField()
    website = models.URLField()
    diversity = models.DecimalField(max_digits=2)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.name

