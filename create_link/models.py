from django.db import models

# Create your models here.
class ShortLink(models.Model):
    long_link = models.CharField(max_length = 255,null = True)
    short_link = models.CharField(max_length = 5)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length = 100,null=False,default = "me")

    def __str__(self) -> str:
        return self.long_link