import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

class ExcelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chromatographic Peaks Deconvolution")
        self.geometry("600x400")
        self.configure(bg="#1e1e2f")
        self.resizable(False, False)

        self.file_path = None
        self.sheet_names = []
        self.selected_sheet = tk.StringVar()
        self.result = None

        self.style = self.setup_style()

        self.start_frame = self.create_start_frame()
        self.sheet_frame = self.create_sheet_frame()
        self.show_frame(self.start_frame)

    def setup_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')

        # Global widget styles
        style.configure('TFrame', background="#1e1e2f")
        style.configure('TLabel', background="#1e1e2f", foreground="#ffffff", font=('Segoe UI', 12))
        style.configure('TButton', background="#3a3a5f", foreground="#ffffff", font=('Segoe UI', 11, 'bold'), padding=10)
        style.map('TButton',
                  background=[('active', '#50507a')],
                  relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
        style.configure('TCombobox',
                        fieldbackground="#ffffff",
                        background="#ffffff",
                        font=('Segoe UI', 11))
        return style

    def create_start_frame(self):
        frame = ttk.Frame(self, padding=30)
        ttk.Label(
            frame,
            text="Deconvolution of Chromatographic Peaks",
            font=('Segoe UI', 16, 'bold'),
            anchor='center',
            wraplength=500
        ).pack(pady=(0, 20))
        ttk.Label(
            frame,
            text="Your data file MUST be in Excel format (.xlsx)",
            anchor='center',
            font=('Segoe UI', 11)
        ).pack(pady=(0, 20))

        button = ttk.Button(frame, text="Select Excel Data File", command=self.pick_file)
        button.pack(pady=(0, 10))
        button.bind("<Enter>", lambda e: button.config(cursor="hand2"))

        return frame

    def create_sheet_frame(self):
        frame = ttk.Frame(self, padding=30)
        ttk.Label(
            frame,
            text="Choose a Sheet to Analyze:",
            font=('Segoe UI', 13, 'bold'),
            anchor='center'
        ).pack(pady=(0, 20))

        self.dropdown = ttk.Combobox(frame, textvariable=self.selected_sheet, state="readonly", width=40)
        self.dropdown.pack(pady=10)
        self.dropdown.bind("<Enter>", lambda e: self.dropdown.config(cursor="hand2"))

        button = ttk.Button(frame, text="OK", command=self.finish_selection)
        button.pack(pady=(20, 10))
        button.bind("<Enter>", lambda e: button.config(cursor="hand2"))

        return frame

    def show_frame(self, frame):
        for widget in self.winfo_children():
            widget.pack_forget()
        frame.pack(expand=True)

    def pick_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            self.file_path = file_path
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
