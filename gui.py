import tkinter as tk
from tkinter import filedialog

#FILE SELECTOR DIALOG
def open_file_dialog(on_file_selected):
    def browse_file(entry, root):
        filepath = filedialog.askopenfilename(
            title="📂 Please select your grading template CSV file",
            filetypes=[("CSV Files", "*.csv")]
        )
        if filepath:
            entry.delete(0, tk.END)
            entry.insert(0, filepath)
            root.destroy()
            on_file_selected(filepath)

    root = tk.Tk()
    root.title("GradeBook - Select Template")
    root.geometry("550x160")
    root.resizable(False, False)

    try:
        icon = tk.PhotoImage(file="assets\icon.png") 
        root.iconphoto(False, icon)
    except:
        pass

    label = tk.Label(root, text="📄 Please select your grading template:")
    label.pack(pady=15)

    file_frame = tk.Frame(root)
    file_frame.pack(pady=5)

    file_entry = tk.Entry(file_frame, width=50)
    file_entry.pack(side=tk.LEFT, padx=(0, 10))

    browse_button = tk.Button(
        file_frame, text="Browse...",
        command=lambda: browse_file(file_entry, root)
    )
    browse_button.pack(side=tk.LEFT)

    root.mainloop()
