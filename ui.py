import tkinter as tk
from tkinter import filedialog, ttk

def get_excel_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx")])
    root.destroy()
    return file_path

def ask_sheet_name(sheet_names):
    root = tk.Tk()
    root.withdraw()

    selected_sheet = tk.StringVar()

    def submit():
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Select Sheet")
    tk.Label(popup, text="Choose a sheet:").pack(pady=10)
    dropdown = ttk.Combobox(popup, textvariable=selected_sheet, values=sheet_names, state="readonly")
    dropdown.pack(pady=5)
    dropdown.current(0)
    tk.Button(popup, text="OK", command=submit).pack(pady=10)

    popup.grab_set()
    root.wait_window(popup)
    root.destroy()

    return selected_sheet.get() if selected_sheet.get() else sheet_names[0]
