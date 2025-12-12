import datetime
from models.project import Project
from tkinter import *
import tkinter as tk
from tkinter import ttk

from exporters.tagsexporter import TagsExporter
from exporters.formataexporter import FormatAExporter
from exporters.formatbexporter import FormatBExporter
from exporters.formatcexporter import FormatCExporter

from repository import Repository
from winforms.projecteditorwindow import ProjectEditorWindow

class ProjectOverviewWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.repository = Repository().set_file_path("projects.json")
        self.projects = self._load_data()
        self.project_in_edit_mode_index = None

        self.title('Personal Project Log')
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        frame_treeview = ttk.Frame(self, padding=10)

        self.treeview = ttk.Treeview(frame_treeview, column=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show='headings', height=5)

        scroll_bar = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scroll_bar.set)

        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview.heading("#1", text="Index")
        self.treeview.column("#1")
        self.treeview.heading("#2", text="Titel", anchor=CENTER)
        self.treeview.column("#3", anchor='e', width=50)
        self.treeview.heading("#3", text="Start", anchor=CENTER)
        self.treeview.column("#4", anchor='e', width=50)
        self.treeview.heading("#4", text="Ende", anchor=CENTER)
        self.treeview.column("#5", anchor='w', width=100)
        self.treeview.heading("#5", text="Kundenname", anchor=CENTER)
        self.treeview.column("#6", anchor='w', width=100)
        self.treeview.heading("#6", text="Kundenstandort", anchor=CENTER)
        self.treeview.column("#7", anchor='w', width=100)
        self.treeview.heading("#7", text="Industriesektor", anchor=CENTER)
        self.treeview['displaycolumns'] = (
            "#2",
            "#3",
            "#4",
            "#5",
            "#6",
            "#7"
        )
        self.treeview.pack()

        frame_treeview.pack(fill=tk.BOTH, expand=True)

        export_format_labels = [
            'Format A',
            'Format B',
            'Format C',
            'Tags'
        ]

        frame_buttons = ttk.Frame(self, padding=10)
        ttk.Button(frame_buttons, text="Neu", command=self._button_create_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Bearbeiten", command=self._button_edit_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Löschen", command=self._button_delete_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Speichern", command=self._button_save_clicked).pack(side=tk.LEFT, padx=5)
        self.combobox_formats = ttk.Combobox(frame_buttons, values=export_format_labels)
        self.combobox_formats.set('Format A')
        self.combobox_formats.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Export", command=self._button_export_clicked).pack(side=tk.LEFT, padx=5)
        frame_buttons.pack()

        self._refresh()
    
    def _load_data(self):
        return self.repository.load()

    def _button_create_clicked(self):
        project_editor_window = ProjectEditorWindow(self, create_project=self.create_project)
        project_editor_window.grab_set()

        self._refresh()
    
    def _button_edit_clicked(self):
        selected_item_iids = self.treeview.selection()

        if selected_item_iids is None or \
            len(selected_item_iids) == 0:
            return
        
        selected_item = self.treeview.item(selected_item_iids[0])
        selected_item_values = selected_item.get('values')

        self.project_in_edit_mode_index = selected_item_values[0]
        self.project_editor_window = ProjectEditorWindow(self, project=self.projects[self.project_in_edit_mode_index], update_project=self.update_project)
        self.project_editor_window.grab_set()

        self._refresh()
    
    def _button_delete_clicked(self):
        selected_item_iids = self.treeview.selection()

        if selected_item_iids is None or \
            len(selected_item_iids) == 0:
            return
        
        selected_item = self.treeview.item(selected_item_iids[0])
        selected_item_values = selected_item.get('values')

        self.projects.pop(selected_item_values[0])
        self._refresh()

    def _button_export_clicked(self):
        exporter = None

        if self.combobox_formats.get() == 'Format A':
            exporter = FormatAExporter()
        elif self.combobox_formats.get() == 'Format B':
            exporter = FormatBExporter()
        elif self.combobox_formats.get() == 'Format C':
            exporter = FormatCExporter()
        elif self.combobox_formats.get() == 'Tags':
            exporter = TagsExporter()
        else:
            return

        exporter\
            .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}_Projekte_{self.combobox_formats.get()}.docx")\
            .export(self.projects)
        
    def _refresh(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for i,project in enumerate(self.projects):
            self.treeview.insert('', 'end', values=(\
                i,\
                project.Title,\
                project.StartDate,\
                project.EndDate,\
                project.CustomerName,\
                project.CustomerLocation,\
                project.IndustrySector\
            ))

    def _button_save_clicked(self):
        self.repository.save(self.projects)

    def create_project(self, project):
        self.projects.append(project)
        self._refresh()

    def update_project(self, project):
        self.projects[self.project_in_edit_mode_index] = project
        self._refresh()