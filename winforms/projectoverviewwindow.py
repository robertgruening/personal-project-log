import datetime
from models.project import Project
from tkinter import *
import tkinter as tk
from tkinter import ttk

from exporters.tagsexporter import TagsExporter
from exporters.formataexporter import FormatAExporter
from exporters.formatbexporter import FormatBExporter
from exporters.formatcexporter import FormatCExporter

from winforms.projecteditorwindow import ProjectEditorWindow

class ProjectOverviewWindow(tk.Tk):
    def __init__(self, projecs:list):
        super().__init__()
        self.projects = projecs

        self.title('Personal Project Log')
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        frame_treeview = ttk.Frame(self, padding=10)

        self.treeview = ttk.Treeview(frame_treeview, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)

        scroll_bar = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scroll_bar.set)

        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview.column("# 1", anchor='w', width=200)
        self.treeview.heading("# 1", text="Titel", anchor=CENTER)
        self.treeview.column("# 2", anchor='e', width=50)
        self.treeview.heading("# 2", text="Start", anchor=CENTER)
        self.treeview.column("# 3", anchor='e', width=50)
        self.treeview.heading("# 3", text="Ende", anchor=CENTER)
        self.treeview.column("# 4", anchor='w', width=100)
        self.treeview.heading("# 4", text="Kundenname", anchor=CENTER)
        self.treeview.column("# 5", anchor='w', width=100)
        self.treeview.heading("# 5", text="Kundenstandort", anchor=CENTER)
        self.treeview.column("# 6", anchor='w', width=100)
        self.treeview.heading("# 6", text="Industriesektor", anchor=CENTER)
        self.treeview.pack()

        for project in self.projects:
            self.treeview.insert('', 'end', values=(\
                project.Title,\
                project.StartDate,\
                project.EndDate,\
                project.CustomerName,\
                project.CustomerLocation,\
                project.IndustrySector\
            ))

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
        self.combobox_formats = ttk.Combobox(frame_buttons, values=export_format_labels)
        self.combobox_formats.set('Format A')
        self.combobox_formats.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Export", command=self._button_export_clicked).pack(side=tk.LEFT, padx=5)
        frame_buttons.pack()
    
    def _button_create_clicked(self):
        project_editor_window = ProjectEditorWindow(self)
        project_editor_window.grab_set()
    
    def _button_edit_clicked(self):
        selected_item_iids = self.treeview.selection()

        if selected_item_iids is None or \
            len(selected_item_iids) == 0:
            return
        
        selected_item = self.treeview.item(selected_item_iids[0])
        selected_item_values = selected_item.get('values')

        for project in self.projects:
            if selected_item_values[0] == project.Title:
                project_editor_window = ProjectEditorWindow(self, project=project)
                project_editor_window.grab_set()
    
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