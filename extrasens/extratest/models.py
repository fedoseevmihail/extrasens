from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint

class Extrasens_1(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    @staticmethod
    def randint_1():
        return str(randint(10, 99))

    @receiver(post_save, sender=User)
    def create_latest_inputs(sender, instance, created, **kwargs):
        if created:
            Extrasens_1.objects.create(user=instance)