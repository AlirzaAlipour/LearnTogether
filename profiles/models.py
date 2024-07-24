from django.db import models
from django.conf import settings
import uuid


class Subject (models.Model):
    title = models.CharField(max_length=255)
class TeacherProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=555)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=12)
    

class StudentProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=11)