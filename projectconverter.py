from models.project import Project
from models.taskgroup import TaskGroup


class ProjectConverter():
    def __init__(self):
        pass

    def convert(self, json_projects):
        projects = []

        for json_project in json_projects:
            project = Project()
            project.Title = json_project.get('Title')
            project.StartDate = json_project.get('StartDate')
            project.EndDate = json_project.get('EndDate')
            project.Description = json_project.get('Description')
            project.CustomerName = json_project.get('CustomerName')
            project.CustomerLocation = json_project.get('CustomerLocation')
            project.IndustrySector = json_project.get('IndustrySector')

            for json_role in json_project.get('RoleNames'):
                project.RoleNames.append(json_role)

            for json_task_group in json_project.get('TaskGroups'):
                task_group = TaskGroup()
                task_group.Name = json_task_group.get('Name')
                
                for json_task in json_task_group.get('Tasks'):
                    task_group.Tasks.append(json_task)

                project.TaskGroups.append(task_group)

            for json_tag in json_project.get('Tags'):
                project.Tags.append(json_tag)

            projects.append(project)

        return projects