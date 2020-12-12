from .models import Student, Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'mark']

class StudentSerialzier(serializers.ModelSerializer):
    #subjects = SubjectSerializer(many = True)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'index', 'dob', 'address', 'year']



