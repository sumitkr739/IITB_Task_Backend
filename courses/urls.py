from django.urls import path
from .views import CourseListCreate, CourseDetail, CourseInstanceListCreate, CourseInstanceDetail

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('instances/', CourseInstanceListCreate.as_view(), name='instance-list-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceDetail.as_view(), name='instance-detail'),
]
