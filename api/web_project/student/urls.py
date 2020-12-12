from django.urls import path
from .views import StudentAPI

app_name = 'student'

urlpatterns = [
    path('', StudentAPI.as_view()),
    path('<int:id>/', StudentAPI.as_view())
]