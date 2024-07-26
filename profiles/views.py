from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import TeacherProfileSerializer, SubjectSerializer
from .models import TeacherProfile, Subject
# Create your views here.
 
class TeacherProfileViewset(ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    

class SubjectViewset(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer