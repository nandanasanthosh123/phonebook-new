from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Use CharField

    def __str__(self):
        return self.name