from .models import TeacherProfile, Subject
from rest_framework import serializers



class TeacherProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class SubjectSerializer (serializers.ModelSerializer):
    available_teachers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='teacherprofile-detail',  # Adjust this to match your URL configuration
    )

    class Meta:
        model = Subject
        fields = ["id", "title", "available_teachers"]