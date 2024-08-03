from django.http.response import HttpResponseForbidden
from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
import json
from rest_framework.authtoken.models import Token
from .decorators import jwt_required
from django.contrib.auth import get_user_model
User = get_user_model()


@jwt_required
def join_chat(request, pk):
    if request.user.is_authenticated:
        teacher = get_object_or_404(User, username=pk)
        #teacher_username = request.GET.get('teacher_username')
        # User is authenticated, proceed with the WebSocket connection
        return render(request, 'communications/join_chat.html', {'myusername_json': mark_safe(json.dumps(request.user.username)),
                                                                 'receiver_json': mark_safe(json.dumps(teacher.username)) })
    else:
        return HttpResponseForbidden()
    
