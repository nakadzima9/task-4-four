from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Course
from .serializers import CourseListSerializer, CourseDetailSerializer

class CourseListView(APIView):
    
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CourseListSerializer(data=request.data)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):

    def get_object(self, pk, format=None):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)
    
    def delete(self, request, pk ,formatn=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)