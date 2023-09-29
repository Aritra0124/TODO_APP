import asana
from asana.rest import ApiException
from django.conf import settings


class AsanaConfig:
    def __init__(self):
        self.configuration = asana.Configuration()
        self.configuration.access_token = settings.ASANA_TOKEN
        self.api_client = asana.ApiClient(self.configuration)

class Project(AsanaConfig):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class to initialize the AsanaConfig
        self.api_instance = asana.ProjectsApi(self.api_client)

    def get_project_name(self, archived=False):
        try:
            # Get multiple projects
            api_response = self.api_instance.get_projects(archived=archived, opt_fields=['name'])
            data = {
                "gid": api_response.data[0].gid,
                "project_name": api_response.data[0].name
            }
            return data
        except ApiException as e:
            print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
            return "Error"
class Task(AsanaConfig):
    def __init__(self):
        super().__init__()
        self.api_instance = asana.TasksApi(self.api_client)

    def get_task_name(self, project_gid):
        try:
            # Get multiple tasks
            api_response = self.api_instance.get_tasks_for_project(project_gid, opt_fields=['name', 'memberships.section.name'])
            task_data = []
            for data in api_response.data:
                task_data.append({
                    "task_name" : data.name,
                    "task_gid": data.gid,
                    "task_section_name": data.memberships[0].section.name
                })
            return task_data
        except ApiException as e:
            print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
            return "Error"

    def get_sections(self, guid):
        try:
            # Get sections in a project
            api_response = self.api_instance.get_sections_for_project(guid, opt_fields=['name'])
            project_sections = []
            for data in api_response:
                project_sections.append({
                    "section_gig": data.gid,
                    "section_name": data.name
                })
            return project_sections
        except ApiException as e:
            print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)

    def create_task(self, data: dict):
        try:
            # Create a task
            body = asana.TasksBody(data)
            api_response = self.api_instance.create_task(body, opt_fields=['name', 'memberships.section.name'])
            print(api_response.data.gid)
            return api_response.data.gid
        except ApiException as e:
            print("Exception when calling TasksApi->create_task: %s\n" % e)

    def delete_task(self, task_gid):
        try:
            # Delete a task
            api_response = self.api_instance.delete_task(task_gid)
            return "deleted"
        except ApiException as e:
            print("Exception when calling TasksApi->delete_task: %s\n" % e)
            return "error"