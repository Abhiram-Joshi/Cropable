from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Crop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # crop = models.CharField(max_length=20)
    # place = models.CharField(max_length=20)
    # photo = models.ImageField(upload_to="crop_images", blank=True)
    # min_price = models.IntegerField()
    # highest_bid = models.IntegerField(default=0)
    # stock = models.IntegerField()
    # description = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="crop_images", blank=True)
    disease = models.CharField(max_length=1000, default="")
    remedy = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.crop

    # def get_absolute_url(self):
    #     return reverse("webpage:home", kwargs={"success": self.pk})