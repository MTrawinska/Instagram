from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Photo(models.Model):
    path = models.ImageField()
    creation_date = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    misa_like_it = models.IntegerField(default=0)
    likers = models.ManyToManyField(User, related_name='likers')

    class Meta:
        ordering = ['creation_date']
