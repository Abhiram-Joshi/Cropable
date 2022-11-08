from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class ReminderModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    # photo = models.ImageField(upload_to="reminder_images", blank=True, null=True)

    def __str__(self):
        return self.title