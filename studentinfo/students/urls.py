from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('student-info/<str:username>/', views.student_info, name='student_info'),
]