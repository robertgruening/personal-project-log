import json
from projectconverter import ProjectConverter


class Repository():
    def __init__(self):
        self.file_path = None

    def set_file_path(self, file_path):
        self.file_path = file_path

        return self

    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            json_projects = json.load(f)
            projects = ProjectConverter().convert(json_projects)
            
            return projects

        return []
    
    def save(self, projects:list):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json_projects = ProjectConverter().convert_to_json(projects)
            json_string_projects = json.dumps(json_projects, indent=4)
            f.write(json_string_projects)
