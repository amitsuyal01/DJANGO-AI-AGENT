from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL
# Create your models here.
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default='title')
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, blank=True, auto_now=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Document- {self.title}>"

    def save(self, *args, **kwargs):
        if self.active and not self.active_at:
            self.active_at = timezone.now()
        elif not self.active:
            self.active_at = None
        super().save(*args, **kwargs)