from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import Filter
from rest_framework.filters import SearchFilter,OrderingFilter


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','course']




    # filter_backends = [SearchFilter]
    # search_fields = ['name', 'course']

    # filterset_fields = ['name']

    # # def get_queryset(self):
    # #     user=self.request.user
    # #     return Student.objects.filter(passed_by=user)
       

       
