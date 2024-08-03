from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import TeacherProfileSerializer, SubjectSerializer
from .models import TeacherProfile, Subject
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
 
class TeacherProfileViewset(ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'], url_path='chat')
    def chat_redirect(self, request, pk):
        teacher_profile = get_object_or_404(TeacherProfile, pk=pk)
        username = teacher_profile.user.username

        # Redirect to the chat URL in the communications app
        chat_url = reverse('communications:join_chat', args=[username])
        return redirect(chat_url)

    

class SubjectViewset(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

