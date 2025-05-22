import tkinter as tk
from tkinter import filedialog, ttk

class ExcelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chromatographic Peaks Deconvolution")
        self.geometry("600x400")
        self.file_path = None
        self.sheet_names = []
        self.selected_sheet = tk.StringVar()
        self.result = None

        self.start_frame = self.create_start_frame()
        self.sheet_frame = self.create_sheet_frame()
        self.show_frame(self.start_frame)

    def create_start_frame(self):
        frame = tk.Frame(self)
        tk.Label(frame, text="Welcome to the Deconvolution of Chromatographic Peaks Program").pack(pady=10)
        tk.Label(frame, text="Your data file MUST be in Excel format.").pack(pady=10)
        tk.Button(frame, text="Select Excel Data File", command=self.pick_file).pack(pady=10)
        return frame

    def create_sheet_frame(self):
        frame = tk.Frame(self)
        tk.Label(frame, text="Choose the sheet that you'll be analyzing:").pack(pady=10)
        self.dropdown = ttk.Combobox(frame, textvariable=self.selected_sheet, state="readonly")
        self.dropdown.pack(pady=5)
        tk.Button(frame, text="OK", command=self.finish_selection).pack(pady=10)
        return frame

    def show_frame(self, frame):
        for widget in self.winfo_children():
            widget.pack_forget()
        frame.pack(expand=True)

    def pick_file(self):
        file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.file_path = file_path
            import pandas as pd
            self.sheet_names = pd.ExcelFile(file_path).sheet_names
            self.dropdown['values'] = self.sheet_names
            self.selected_sheet.set(self.sheet_names[0])
            self.show_frame(self.sheet_frame)

    def finish_selection(self):
        self.result = (self.file_path, self.selected_sheet.get())
        self.quit()

def get_excel_file_and_sheet():
    app = ExcelApp()
    app.mainloop()
    return app.result
