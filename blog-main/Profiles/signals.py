import email
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile




@receiver(post_save, sender = User)
def my_post_save(sender, instance, created, **kwargs):
    print("sender: ",sender)
    print("instance: ", instance)
    if created:
        Profile.objects.create(user = instance, email = instance.email)