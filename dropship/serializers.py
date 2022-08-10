from dataclasses import field
from email.policy import default
from pyexpat import model
from .models import Issue, Project, User
from rest_framework import serializers

class IssueSerializers(serializers.ModelSerializer) :
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Issue
        fields = "__all__"

class ProjectSerializers(serializers.ModelSerializer) :
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer) :
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = User
        fields = "__all__"