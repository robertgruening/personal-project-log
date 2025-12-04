import docx

class TagsExporter():
    def __init__(self):
        self.file_path = None

    def set_file_path(self, file_path:str):
        self.file_path = file_path

        return self

    def export(self, projects:list):
        tags = []

        for i, project in enumerate(projects):
            for tag in project.Tags:
                if tag not in tags:
                    tags.append(tag)

        doc = docx.Document()
        run_tags = doc.add_paragraph(style=None)\
            .add_run('Tags')
        run_tags.bold = True

        tags.sort()

        for tag in tags:
            doc.add_paragraph(style='List Bullet')\
                .add_run(tag)

        doc.save(self.file_path)