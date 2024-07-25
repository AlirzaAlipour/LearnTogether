from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import TeacherProfile, StudentProfile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            if instance.user_type == 'teacher':
                TeacherProfile.objects.create(user=instance, subject=None)
            elif instance.user_type == 'student':
                StudentProfile.objects.create(user=instance)
        except Exception as e:
            logger.error(f"Error creating profile for {instance.username}: {e}")