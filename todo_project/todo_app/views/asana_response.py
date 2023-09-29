from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..views.asana_connection import Project, Task
@api_view(['GET'])
def test_response(request):
    if request.method == 'GET':
        asana_project = Project()
        data = {"project": asana_project.get_project_name()}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['GET'])
def task_response(request):
    if request.method == 'GET':
        project_gid = request.GET.get("gid")
        asana_project = Task()
        data = {"task": asana_project.get_task_name(project_gid)}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_section_names(request):
    if request.method == 'GET':
        project_gid = request.GET.get("gid")
        asana_project = Task()
        data = {"sections": asana_project.get_sections(project_gid)}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        project_gid = request.POST.get("project_gid")
        task_name = request.POST.get("task_name")
        asana_project = Task()
        data = {"task_gid": asana_project.create_task({"name": task_name, "projects": project_gid})}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['GET'])
def task_delete(request):
    if request.method == 'GET':
        project_gid = request.GET.get("gid")
        asana_project = Task()
        data = {"task": asana_project.delete_task(project_gid)}
        return Response(data=data, status= status.HTTP_200_OK)