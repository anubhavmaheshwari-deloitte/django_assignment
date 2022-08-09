import json
from tokenize import Token
from django.db import router
from django.forms import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from dropship.permissions import IsOwner

from dropship.settings import ALLOWED_HOSTS
from .serializers import IssueSerializers, ProjectSerializers, UserSerializers
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Issue, Project, User

class MyViewSet (viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

class IssueViewset(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    permission_classes = [IsOwner]

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    permission_classes = [IsOwner]

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsOwner]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllIssues(request):
    issues = Issue.objects.all()
    data=IssueSerializers(issues, many=True)
    return Response(data.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getIssue(request, id):
    issue = Issue.objects.filter(id=id)
    data=IssueSerializers(issue, many=True)
    print(data)
    return Response(data.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createIssue(request):
    newIssue = IssueSerializers(data = request.data)
    if newIssue.is_valid() :
        newIssue.save()
        return Response(newIssue.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateIssue(request,id):

    issue = Issue.objects.filter(id=id)
    data=IssueSerializers(instance=issue, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        print(data)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteIssue(request,id):
    issue = Issue.objects.filter(id=id)
    issue.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllProjects(request):
    projects = Project.objects.all()
    data=ProjectSerializers(projects, many=True)
    return Response(data.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request, id):
    project = Project.objects.filter(id=id)
    data=ProjectSerializers(project, many=True)
    return Response(data.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProject(request):
    newProject = ProjectSerializers(data = request.data)
    if newProject.is_valid() :
        newProject.save()
        return Response(newProject.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProject(request,id):
    project = Project.objects.filter(id=id)
    data=ProjectSerializers(instance=project, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProject(request,id):
    project = Project.objects.filter(id=id)
    project.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
