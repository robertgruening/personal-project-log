from models.project import Project
from tkinter import *
import tkinter as tk
from tkinter import ttk


class ProjectEditorWindow(tk.Toplevel):
    def __init__(self, parent, project=None):
        super().__init__(parent)

        self.project = project
        self.title('Projekt')

        #region title
        title_label = ttk.Label(self, text="Titel")
        title_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

        title_entry = ttk.Entry(self)
        title_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            title_entry.insert(0, self.project.Title)
        #endregion

        #region start date
        start_date_label = ttk.Label(self, text="Startdatum")
        start_date_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        start_date_entry = ttk.Entry(self)
        start_date_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            start_date_entry.insert(0, self.project.StartDate)
        #endregion

        #region end date
        end_date_label = ttk.Label(self, text="Enddatum")
        end_date_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

        end_date_entry = ttk.Entry(self)
        end_date_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            end_date_entry.insert(0, self.project.EndDate)
        #endregion

        #region button save
        frame_buttons = ttk.Frame(self, padding=10)
        ttk.Button(frame_buttons, text="Abbrechen", command=self.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Speichern").pack(side=tk.LEFT, padx=5)
        frame_buttons.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        #endregion