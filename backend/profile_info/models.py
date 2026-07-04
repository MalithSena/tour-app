from django.db import models

class Profile(models.Model):
    photo = models.ImageField(upload_to='profile/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile photo (updated {self.updated_at.strftime('%Y-%m-%d')})"