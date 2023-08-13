from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Connection Issue', 'Connection Issue'),
        ('New Connection', 'New Connection'),
    ]

    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(choices=SERVICE_TYPES, max_length=50)
    details = models.TextField()
    attached_file = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.service_type}"
