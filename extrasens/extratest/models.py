from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from random import randint


class Extrasens(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    
    @receiver(post_save, sender=User)
    def create_latest_inputs_1(sender, instance, created, **kwargs):
        if created:
            Extrasens.objects.create(user=instance)

    def __str__(self):
        return self.user
    
class NumUser(models.Model):
    number = models.CharField(max_length=2, verbose_name='Введите загаданное число', null=True)

    def __str__(self):
        return self.number
    
class Extrasens_1(models.Model):
    reliability = models.CharField(max_length=2, null=True)
    number = models.CharField(max_length=2, null=True)
        
    @staticmethod
    def randint():
        return randint(10, 99)
    
    def __str__(self):
        return self.number
    
class Extrasens_2(models.Model):
    reliability = models.CharField(max_length=2, null=True)
    number = models.CharField(max_length=2, null=True)
        
    @staticmethod
    def randint():
        return randint(10, 99)
    
    def __str__(self):
        return self.number
