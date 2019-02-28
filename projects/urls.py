from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index),
    path('login', views.login_view),
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/<project_uid>/', views.project_view),
    path('approval', views.ApprovalView.as_view(), name='approval')
]
