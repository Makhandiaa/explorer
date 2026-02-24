from django.db import models
from django.contrib.auth.models import User


class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserCounty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'county')

    def __str__(self):
        return f"{self.user.username} visited {self.county.name}"
