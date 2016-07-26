from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
# from grader.models import Assignment
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from grader.serializers import UserSerializer, GroupSerializer
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Submission(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, assignment_name):
        dump_data = {}
        dump_data["assignment"] = assignment_name
        dump_data["correct"] = True
        dump_data["score"] = 1
        dump_data["msg"] = "<p>The code passed all tests.</p>"

        return HttpResponse(json.dumps(dump_data), content_type='application/json')
