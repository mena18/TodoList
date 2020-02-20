from django.urls import path
from .views import *

app_name="todo"

urlpatterns = [

    path("",home,name='home'),
    path("toogle_finishing",toogle_finishing,name='finish'),

    # taso create,edit,delete
    path("task/create",CreateTask.as_view(),name='create_task'),
    path("task/edit/<pk>",EditTask.as_view(),name='edit_task'),
    path("task/delete/<pk>",DeleteTask,name='delete_task'),

    # project create,edit,delete,show
    path("project/create",CreateProject.as_view(),name='create_project'),
    path("project/edit/<pk>",EditProject.as_view(),name='edit_project'),
    path("project/delete/<pk>",DeleteProject,name='delete_project'),
    path("project/<pk>",ViewProject,name='view_project'),
    path("projects",ViewProjects,name='all_projects'),

    # Folder create,edit,delete
    path("list/create",CreateList.as_view(),name='create_list'),
    path("list/edit/<pk>",EditList.as_view(),name='edit_list'),
    path("list/delete/<pk>",DeleteList,name='delete_list'),
    path("list/<pk>",ViewList,name='view_list'),
    path("lists",ViewLists,name='all_lists'),


    path("create_many",create_many,name='create_many'),

]
