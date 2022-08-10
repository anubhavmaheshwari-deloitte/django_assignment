"""dropship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dropship import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('issues/',views.getAllIssues , name='issues'),
    path('issues/<int:id>/',views.getIssue, name='issue'),
    path('issues/create/', views.createIssue, name='createIssue'),
    path('issues/<int:id>/update/',views.updateIssue, name='updateIssue'),
    path('issues/<int:id>/delete/', views.deleteIssue, name='deleteIssue'),
    path('projects/',views.getAllProjects , name='projects'),
    path('projects/<int:id>/',views.getProject, name='project'),
    path('projects/create/', views.createProject, name='createProject'),
    path('projects/<int:id>/update/',views.updateProject, name='updateProject'),
    path('projects/<int:id>/delete/', views.deleteProject, name='deleteProject'),
    path('projects/<int:pid>/issues/',views.getAllIssuesUnderProject , name='issuesUnderProject'),
    path('projects/<int:pid>/issues/<int:iid>/',views.getIssueUnderProject, name='issueUnderProject'),
    path('projects/<int:pid>/issues/create/', views.createIssueUnderProject, name='createIssueUnderProject'),
    path('projects/<int:pid>/issues/<int:iid>/update/',views.updateIssueUnderProject , name='updateIssueUnderProject'),
    path('projects/<int:pid>/issues/<int:iid>/delete/', views.deleteIssueUnderProject, name='deleteIssuePnderProject'),
]