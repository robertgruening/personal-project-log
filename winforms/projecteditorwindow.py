from models.project import Project
from tkinter import *
import tkinter as tk
from tkinter import ttk

class ProjectEditorWindow(tk.Toplevel):
    def __init__(self, parent, project=None, create_project=None, update_project=None):
        super().__init__(parent)

        self.project = project
        self.create_project = create_project
        self.update_project = update_project
        self.title('Projekt')
        row_index = 0

        #region title
        title_label = ttk.Label(self, text="Titel")
        title_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.Title is not None:
            self.title_entry.insert(0, self.project.Title)
        row_index += 1
        #endregion


        #region start date
        start_date_label = ttk.Label(self, text="Startdatum")
        start_date_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.start_date_entry = ttk.Entry(self)
        self.start_date_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.StartDate is not None:
            self.start_date_entry.insert(0, self.project.StartDate)
        row_index += 1
        #endregion

        #region end date
        end_date_label = ttk.Label(self, text="Enddatum")
        end_date_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.end_date_entry = ttk.Entry(self)
        self.end_date_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.EndDate is not None:
            self.end_date_entry.insert(0, self.project.EndDate)
        row_index += 1
        #endregion

        #region customer name
        customer_name_label = ttk.Label(self, text="Kundenname")
        customer_name_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.customer_name_entry = ttk.Entry(self)
        self.customer_name_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.CustomerName is not None:
            self.customer_name_entry.insert(0, self.project.CustomerName)
        row_index += 1
        #endregion

        #region customer location
        customer_location_label = ttk.Label(self, text="Kundenstandort")
        customer_location_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.customer_location_entry = ttk.Entry(self)
        self.customer_location_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.CustomerLocation is not None:
            self.customer_location_entry.insert(0, self.project.CustomerLocation)
        row_index += 1
        #endregion

        #region industry sector
        industry_sector_label = ttk.Label(self, text="Industriesektor")
        industry_sector_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.industry_sector_entry = ttk.Entry(self)
        self.industry_sector_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.IndustrySector is not None:
            self.industry_sector_entry.insert(0, self.project.IndustrySector)
        row_index += 1
        #endregion

        #region description
        description_label = ttk.Label(self, text="Beschreibung")
        description_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.description_entry = Text(self, height=10)
        self.description_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.Description is not None:
            self.description_entry.insert(END, self.project.Description)
        row_index += 1
        #endregion

        #region tags
        tags_label = ttk.Label(self, text="Tags")
        tags_label.grid(column=0, row=row_index, sticky=tk.EW, padx=5, pady=5)

        self.tags_entry = Text(self, height=10)
        self.tags_entry.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=5)
        
        if self.project is not None and\
            self.project.Tags is not None:
            self.tags_entry.insert(END, ', '.join(self.project.Tags))
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
        project.IndustrySector = self.industry_sector_entry.get()
        project.Description = self.description_entry.get("1.0", "end")
        tags = self.tags_entry.get("1.0", "end").split(',')
        trimmed_tags = []

        for tag in tags:
            trimmed_tag = tag.strip(' ')
            trimmed_tag = trimmed_tag.strip('\n')
            trimmed_tags.append(trimmed_tag)

        project.Tags = trimmed_tags

        # validate project

        # return to main window
        if self.project is None:
            self.create_project(project)
        else:
            self.update_project(project)
        
        self.destroy()