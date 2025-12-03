import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
#from json import JSONEncoder

from formataexporter import FormatAExporter
from projectconverter import ProjectConverter
from repository import Repository

#class ProjectEncoder(JSONEncoder):
#    def default(self, o):
#        return o.__dict__

def export_to_format_a():
    FormatAExporter()\
        .set_file_path(f"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S_Projekte.docx")}")\
        .export(projects)

json_projects = Repository()\
    .set_file_path("projects.json")\
    .load()

projects = ProjectConverter()\
    .convert(json_projects)
    
window = Tk()
window.title('Personal Project Log')

frame_treeview = ttk.Frame(window, padding=10)

treeview = ttk.Treeview(frame_treeview, column=("c1", "c2", "c3"), show='headings', height=5)

scroll_bar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
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

frame_treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_buttons = ttk.Frame(window, padding=10)
ttk.Button(frame_buttons, text="Export (Format A)", command=export_to_format_a).grid(column=0, row=0)
frame_buttons.pack()

window.mainloop()