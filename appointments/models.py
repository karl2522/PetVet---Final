from django.db import models


# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('REJECTED', 'Rejected'),
    ]

    SERVICE_CHOICES = [
        ('CHECKUP', 'General Check-up'),
        ('VACCINATION', 'Vaccination'),
        ('SURGERY', 'Surgery'),
        ('GROOMING', 'Grooming'),
        ('DENTAL', 'Dental Care'),
        ('EMERGENCY', 'Emergency Care'),
    ]


    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='CHECKUP')
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.pet.pet_name} - {self.service_type} ({self.date})"