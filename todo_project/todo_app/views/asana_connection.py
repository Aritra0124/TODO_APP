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
            api_response = self.api_instance.get_tasks_for_project(project_gid, opt_fields=['name', 'memberships.section.name', 'notes'])
            task_data = []
            for data in api_response.data:
                task_data.append({
                    "task_name" : data.name,
                    "task_gid": data.gid,
                    "task_note": data.notes,
                    "task_section_name": data.memberships[0].section.name,
                    "task_section_gid": data.memberships[0].section.gid
                })
            return task_data
        except ApiException as e:
            print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
            return "Error"


    def create_task(self, data: dict, section_gid):
        try:
            # Create a task
            body = asana.TasksBody(data)
            api_response = self.api_instance.create_task(body, opt_fields=['name', 'memberships.section.name'])
            if section_gid != 0:
                update_section = Section()
                update_section.update_task_section(section_gid, api_response.data.gid)
            return "Successfully Created"
        except ApiException as e:
            print("Exception when calling TasksApi->create_task: %s\n" % e)

    def edit_task(self, task_gid, data, section_gid):
        try:
            # Update a task
            body = asana.TasksTaskGidBody(data)
            api_response = self.api_instance.update_task(body, task_gid, opt_fields=['name'])
            if section_gid != 0:
                update_section = Section()
                update_section.update_task_section(section_gid, task_gid)
            return "Successfully Updated"
        except ApiException as e:
            print("Exception when calling TasksApi->update_task: %s\n" % e)

    def delete_task(self, task_gid):
        try:
            # Delete a task
            api_response = self.api_instance.delete_task(task_gid)
            return "deleted"
        except ApiException as e:
            print("Exception when calling TasksApi->delete_task: %s\n" % e)
            return "error"
class Section(AsanaConfig):
    def __init__(self):
        super().__init__()
        self.api_instance = asana.SectionsApi(self.api_client)
    def get_sections(self, guid):
        try:
            # Get sections in a project
            api_response = self.api_instance.get_sections_for_project(guid, opt_fields=['name'])
            project_sections = []
            for data in api_response.data:
                project_sections.append({
                    "section_gid": data.gid,
                    "section_name": data.name
                })
            return project_sections
        except ApiException as e:
            print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)

    def update_task_section(self, section_gid, task_gid):
        try:
            body = asana.SectionGidAddTaskBody({"task": task_gid})
            # Add task to section
            api_response = self.api_instance.add_task_for_section(section_gid, body=body)
            return True
        except ApiException as e:
            print("Exception when calling SectionsApi->add_task_for_section: %s\n" % e)
