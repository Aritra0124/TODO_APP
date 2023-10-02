from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..views.asana_connection import Project, Task, Section
from ..models import TodoTask
@api_view(['GET'])
def project_response(request):
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
        for task in data["task"]:
            update, created = TodoTask.objects.update_or_create(
                task_gid=task["task_gid"],
                defaults={
                    'task_name': task["task_name"],
                    'task_note': task["task_note"],
                    'task_section_gid': task["task_section_gid"],
                    'task_section': task["task_section_name"]
                }
            )
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_section_names(request):
    if request.method == 'GET':
        project_gid = request.GET.get("gid")
        asana_project = Section()
        data = {"sections": asana_project.get_sections(project_gid)}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        project_gid = request.POST.get("project_gid")
        task_name = request.POST.get("task_name")
        task_note = request.POST.get("task_note")
        section_gid = request.POST.get("section_gid", 0)
        asana_project = Task()
        data = {"status": asana_project.create_task({"name": task_name, "notes":task_note,"projects": project_gid}, section_gid)}
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['POST'])
def edit_task(request):
    if request.method == 'POST':
        task_gid = request.POST.get("task_gid")
        task_name = request.POST.get("task_name")
        task_note = request.POST.get("task_note")
        section_gid = request.POST.get("section_gid", 0)
        asana_project = Task()
        data = {"status": asana_project.edit_task(task_gid,{"name": task_name, "notes": task_note}, section_gid)}
        TodoTask.objects.filter(task_gid= task_gid).update(task_name=task_name,task_section_gid=section_gid)
        return Response(data=data, status= status.HTTP_200_OK)

@api_view(['GET'])
def task_delete(request):
    if request.method == 'GET':
        task_gid = request.GET.get("gid")
        asana_project = Task()
        data = {"task": asana_project.delete_task(task_gid)}
        TodoTask.objects.get(task_gid= task_gid).delete()
        return Response(data=data, status= status.HTTP_200_OK)