from django.db import models


class Usr(models.Model):
    username = models.CharField(max_length=50)


class Micropost(models.Model):
    user = models.ForeignKey(Usr, on_delete=models.CASCADE,
                             related_name='owner')
    text = models.CharField(max_length=300)
    referenced = models.ForeignKey(Usr, null=True,
                                   on_delete=models.CASCADE,
                                   related_name='reference')
    timestamp = models.DateTimeField(auto_now=True)
