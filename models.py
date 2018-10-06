from django.db import models

# Create your models here.

from django.utils import timezone

class cert(models.Model):
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    system = models.TextField()
    created_date = models.DateField(
            default=timezone.now)
    expiry_date = models.DateField(
            default=timezone.now)

    published_date = models.DateField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
