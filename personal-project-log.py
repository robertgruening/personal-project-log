import datetime
#from json import JSONEncoder

from formataexporter import FormatAExporter
from projectconverter import ProjectConverter
from repository import Repository

#class ProjectEncoder(JSONEncoder):
#    def default(self, o):
#        return o.__dict__

json_projects = Repository()\
    .set_file_path("projects.json")\
    .load()

projects = ProjectConverter()\
    .convert(json_projects)

FormatAExporter()\
    .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte.docx")}")\
    .export(projects)