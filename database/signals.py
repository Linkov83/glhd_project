from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def deactivate_new_users(sender, instance, created, **kwargs):
    if created and instance.is_active:
        instance.is_active = False
        instance.save()