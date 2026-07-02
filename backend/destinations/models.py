from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=[
            ('cultural', 'Cultural'),
            ('wildlife', 'Wildlife'),
            ('hill_country', 'Hill Country'),
        ]
    )
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name