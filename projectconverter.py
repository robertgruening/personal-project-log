from project import Project
from role import Role


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

            for json_role in json_project.get('Roles'):
                role = Role()
                role.Name = json_role.get('Name')

                for json_task in json_role.get('Tasks'):
                    role.Tasks.append(json_task)
                
                project.Roles.append(role)

            for json_tag in json_project.get('Tags'):
                project.Tags.append(json_tag)

            projects.append(project)

        return projects