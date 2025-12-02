import datetime
#from json import JSONEncoder

from formataexporter import FormatAExporter
from projectconverter import ProjectConverter
from repository import Repository

#class ProjectEncoder(JSONEncoder):
#    def default(self, o):
#        return o.__dict__
        
def convert_to_projects(json_projects):
    return ProjectConverter()\
        .convert(json_projects)

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