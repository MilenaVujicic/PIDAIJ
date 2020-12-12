from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models  import Student, Subject
from .serializers import StudentSerialzier

class StudentAPI(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerialzier(students, many = True)
        return Response(serializer.data)
     

    def post(self, request):
        serializer = StudentSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerialzier(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerialzier(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=204)