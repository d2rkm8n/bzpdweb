from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user

    def __str__(self):
        return f'{self.user} - {self.department}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'