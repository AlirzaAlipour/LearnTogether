from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherProfileViewset, SubjectViewset

router = DefaultRouter()
router.register("profiles", TeacherProfileViewset, basename='teacherprofile')
router.register("subjects", SubjectViewset, basename="subjects")

urlpatterns = [
    path("", include(router.urls)),

]