"""OPS1 URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from OPS1 import settings
from OPSApp.views import index, register, login, StudentOTR, welcome, CreateProjectView, projectlist, project_view, \
    updateproject, projectdelete, gprojectlist, gproject_view, approveproject, gprojectdelete, hprojectlist, \
    project_status, happroveproject, searchproject, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('OTR/',StudentOTR.as_view(),name='studentotr'),
    path('welcome/',welcome,name='welcome'),
    path('createproject/',CreateProjectView.as_view(success_url="/welcome"),name='createproject'),
    # path('status/',gstatusview,name='gstatus'),
    path('project/',projectlist,name='userprojectlist'),
    path('projectlist/',gprojectlist,name='gprojectlist'),
    path('projects/',hprojectlist,name='hprojectlist'),
    path('project/<pk>/',project_view,name='projectview'),
    path('projects/<pk>/',gproject_view,name='gprojectview'),
    path('status/<pk>',project_status,name='project_status'),

    path('<pk>/update',updateproject,name='projectupdate'),
    path('<pk>/approve',approveproject.as_view(),name='gapprove'),
    path('<pk>/approve_hod',happroveproject.as_view(),name='happrove'),
    # path('<pk>/happrove',happroveproject,name='happrove'),

    # path('<pk>/approve',approveproject,name='gapprove'),
    path('<pk>/delete',projectdelete,name='projectdelete'),
    path('<pk>/remove',gprojectdelete,name='gdelete'),
    path('projectsall',searchproject,name='searchproject'),
    path('logout',logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
