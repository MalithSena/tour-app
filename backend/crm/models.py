from django.db import models
from django_cryptography.fields import encrypt


class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    passport_number = encrypt(models.CharField(max_length=50))

    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_phone = models.CharField(max_length=50, blank=True)
    emergency_contact_relationship = models.CharField(max_length=100, blank=True)

    notes = models.TextField(blank=True, help_text="Any additional details about this tourist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.nationality})"

    class Meta:
        ordering = ['-created_at']