from models.project import Project
from tkinter import *
import tkinter as tk
from tkinter import ttk

class ProjectEditorWindow(tk.Toplevel):
    def __init__(self, parent, project=None):
        super().__init__(parent)

        self.project = project
        self.title('Projekt')
        row_index = 0

        #region title
        title_label = ttk.Label(self, text="Titel")
        title_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.title_entry.insert(0, self.project.Title)
        row_index += 1
        #endregion


        #region start date
        start_date_label = ttk.Label(self, text="Startdatum")
        start_date_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.start_date_entry = ttk.Entry(self)
        self.start_date_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.start_date_entry.insert(0, self.project.StartDate)
        row_index += 1
        #endregion

        #region end date
        end_date_label = ttk.Label(self, text="Enddatum")
        end_date_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.end_date_entry = ttk.Entry(self)
        self.end_date_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.end_date_entry.insert(0, self.project.EndDate)
        row_index += 1
        #endregion

        #region customer name
        customer_name_label = ttk.Label(self, text="Kundenname")
        customer_name_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.customer_name_entry = ttk.Entry(self)
        self.customer_name_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.customer_name_entry.insert(0, self.project.CustomerName)
        row_index += 1
        #endregion

        #region customer location
        customer_location_label = ttk.Label(self, text="Kundenstandort")
        customer_location_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.customer_location_entry = ttk.Entry(self)
        self.customer_location_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.customer_location_entry.insert(0, self.project.CustomerLocation)
        row_index += 1
        #endregion

        #region description
        description_label = ttk.Label(self, text="Beschreibung")
        description_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.description_entry = Text(self, height=10)
        self.description_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None:
            self.description_entry.insert(END, self.project.Description)
        row_index += 1
        #endregion

        #region button save
        frame_buttons = ttk.Frame(self, padding=10)
        ttk.Button(frame_buttons, text="Abbrechen", command=self.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Übernehmen", command=self.event_button_apply_clicked).pack(side=tk.LEFT, padx=5)
        frame_buttons.grid(column=1, row=row_index, sticky=tk.E, padx=5, pady=5)
        #endregion
    
    def event_button_apply_clicked(self):
        project = Project()
        project.Title = self.title_entry.get()
        project.StartDate = self.start_date_entry.get()
        project.EndDate = self.end_date_entry.get()
        project.CustomerName = self.customer_name_entry.get()
        project.CustomerLocation = self.customer_location_entry.get()
        project.Description = self.description_entry.get("1.0", "end")

        # validate project

        # return to main window
        
        self.destroy()