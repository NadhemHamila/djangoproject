from datetime import date
from django.db import models
from django.utils import timezone
from updater.update import schedule_request
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Scheduler(models.Model):
    request_type = (
        ('POST', 'POST'),
        ('GET', 'GET'),
    )

    status_type = (
        ('scheduled', 'scheduled'),
        ('sent', 'sent'),
    )
    title = models.CharField(max_length=255)
    
    Request = models.CharField(
        max_length=5,
        choices=request_type,
        help_text='Request Type',
        default='GET'
    )
    
    status = models.CharField(max_length=20, choices = status_type, default='scheduled')

    request_body = models.TextField(verbose_name ='Request Body', default='{}',help_text = 'Please fill this field only if you are sending a post request')

    date_to_execute = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender= timezone.now)
    def update_status(self, *args, **kwargs):
        if self.date_to_execute > timezone.now:
            self.status_type = "scheduled"
        elif self.date_to_execute <= timezone.now:
            self.status_type = "sent"
        super(Scheduler, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        schedule_request(self.Request, self.request_body, self.date_to_execute)
        super(Scheduler, self).save(*args, **kwargs)


class Individual(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=30, help_text="Enter the person's name")
    surname = models.CharField(max_length=50, help_text="Enter the person's family name")
    job_title = models.CharField(max_length=50, help_text="Enter the person's job")

    def __str__(self):
        """String for representing the Model object."""
        return self.name
