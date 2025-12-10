#from json import JSONEncoder

from projectconverter import ProjectConverter
from repository import Repository
from winforms.projectoverviewwindow import ProjectOverviewWindow

#class ProjectEncoder(JSONEncoder):
#    def default(self, o):
#        return o.__dict__

json_projects = Repository()\
    .set_file_path("projects.json")\
    .load()

projects = ProjectConverter()\
    .convert(json_projects)

project_overview_window = ProjectOverviewWindow(projects)
project_overview_window.mainloop()