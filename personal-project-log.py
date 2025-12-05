import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
#from json import JSONEncoder

from tagsexporter import TagsExporter
from formataexporter import FormatAExporter
from formatbexporter import FormatBExporter
from formatcexporter import FormatCExporter
from project import Project
from projectconverter import ProjectConverter
from repository import Repository

#class ProjectEncoder(JSONEncoder):
#    def default(self, o):
#        return o.__dict__

def create_project():
    open_project_form()

def edit_project():
    selected_item_iids = treeview.selection()

    if selected_item_iids is None or \
        len(selected_item_iids) == 0:
        return
    
    selected_item = treeview.item(selected_item_iids[0])
    selected_item_values = selected_item.get('values')

    for project in projects:
        if selected_item_values[0] == project.Title:
            open_project_form(project)

def export_tags():
    TagsExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekt-Tags.docx")}")\
        .export(projects)
    
def export_to_format_a():
    FormatAExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte_Format-A.docx")}")\
        .export(projects)
    
def export_to_format_b():
    FormatBExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte_Format-B.docx")}")\
        .export(projects)
    
def export_to_format_c():
    FormatCExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte_Format-C.docx")}")\
        .export(projects)

def open_project_form(project:Project):
    project_form = Tk()
    project_form.title('Projekt')

    #region title
    title_label = ttk.Label(project_form, text="Titel")
    title_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    title_entry = ttk.Entry(project_form)
    title_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
    
    if project is not None:
        title_entry.insert(0, project.Title)
    #endregion

    #region start date
    start_date_label = ttk.Label(project_form, text="Startdatum")
    start_date_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

    start_date_entry = ttk.Entry(project_form)
    start_date_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
    
    if project is not None:
        start_date_entry.insert(0, project.StartDate)
    #endregion

    #region end date
    end_date_label = ttk.Label(project_form, text="Enddatum")
    end_date_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

    end_date_entry = ttk.Entry(project_form)
    end_date_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)
    
    if project is not None:
        end_date_entry.insert(0, project.EndDate)
    #endregion

    #region button save
    frame_buttons = ttk.Frame(project_form, padding=10)
    ttk.Button(frame_buttons, text="Abbrechen").pack(side=tk.LEFT, padx=5)
    ttk.Button(frame_buttons, text="Speichern").pack(side=tk.LEFT, padx=5)
    frame_buttons.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    #endregion

    project_form.mainloop()

json_projects = Repository()\
    .set_file_path("projects.json")\
    .load()

projects = ProjectConverter()\
    .convert(json_projects)

window = Tk()
window.title('Personal Project Log')
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))

frame_treeview = ttk.Frame(window, padding=10)

treeview = ttk.Treeview(frame_treeview, column=("c1", "c2", "c3"), show='headings', height=5)

scroll_bar = ttk.Scrollbar(frame_treeview, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_bar.set)

treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

treeview.column("# 1", anchor='w', width=200)
treeview.heading("# 1", text="Titel", anchor=CENTER)
treeview.column("# 2", anchor='e', width=50)
treeview.heading("# 2", text="Start", anchor=CENTER)
treeview.column("# 3", anchor='e', width=50)
treeview.heading("# 3", text="Ende", anchor=CENTER)
treeview.pack()

for project in projects:
    treeview.insert('', 'end', values=(project.Title, project.StartDate, project.EndDate))

frame_treeview.pack(fill=tk.BOTH, expand=True)

frame_buttons = ttk.Frame(window, padding=10)
ttk.Button(frame_buttons, text="Neu", command=create_project).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Bearbeiten", command=edit_project).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Export (Tags)", command=export_tags).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Export (Format A)", command=export_to_format_a).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Export (Format B)", command=export_to_format_b).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_buttons, text="Export (Format C)", command=export_to_format_c).pack(side=tk.LEFT, padx=5)
frame_buttons.pack()

window.mainloop()