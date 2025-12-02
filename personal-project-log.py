import datetime
from json import JSONEncoder

from repository import Repository
from formataexporter import FormatAExporter

class Role():
    def __init__(self):
        self.Name = None
        self.Tasks = []

class Project():
    def __init__(self):
        self.Title = None
        self.StartDate = None
        self.EndDate = None
        self.Description = None
        self.CustomerName = None
        self.Roles = []
        self.Tags = []

class ProjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
        
def convert_to_projects(json_projects):
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

def load_data():
    return convert_to_projects(
        Repository()\
            .set_file_path("projects.json")\
            .load()
    )

def export_format_a(projects:list):
    FormatAExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte.docx")}")\
        .export(projects)

export_format_a(load_data())