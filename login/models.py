from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=50, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name