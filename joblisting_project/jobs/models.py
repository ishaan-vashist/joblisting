from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateField()
    details_url = models.URLField()

    def __str__(self):
        return self.title
