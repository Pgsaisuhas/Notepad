import os
import tkinter as tk
import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
from pathlib import Path

# --------------------functions--------------------------------------------- #

FILE_LOCATION = ""


def save_file():
    file_location = FILE_LOCATION
    print(file_location)
    file_name = os.path.basename(file_location).split('/')[-1]
    print(file_name)
    if not file_name:
        return
    with open(str(file_name), mode="w") as save_input:
        text = text_edit.get(1.0, tk.END)
        save_input.write(text)


def save_as_file():
    file_location = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt"), ["All files", "*.*"]]
    )
    if not file_location:
        return
    with open(file_location, mode="w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"MY NOTEPAD :{file_location}")


def open_file():
    global FILE_LOCATION
    FILE_LOCATION = askopenfilename(
        filetypes=[("Text Files","*.txt"), ["All files", "*.*"]]
    )
    if not FILE_LOCATION:
        return
    text_edit.delete(1.0, tk.END)
    with open(FILE_LOCATION, mode="r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"MY NOTEPAD: {FILE_LOCATION}")


# -----------------UI SETUP------------------------------------------------ #
root = ctk.CTk()
root.title("MY NOTEPAD")
root.rowconfigure(0, minsize=600)
root.columnconfigure(1, minsize=600)

# text_edit = tk.Text(master=root)
text_edit = ctk.CTkTextbox(master=root)
text_edit.grid(row=0, column=1, sticky="nsew")
frame_button = ctk.CTkFrame(master=root, border_color="blue", border_width=1)
frame_button.grid(row=0,column=0, sticky="nsew")
# open_button = tk.Button(master=frame_button, text="OPEN FILE", command=open_file)
open_button = ctk.CTkButton(
    master=frame_button,
    text="Open File",
    border_color="light blue",
    border_width=2,
    hover_color="blue",
    command=open_file
    )
open_button.grid(row=0, column=0, padx=5, pady=15)

save_button = ctk.CTkButton(
    master=frame_button,
    text="Save",
    border_color="light blue",
    border_width=2,
    hover_color="blue",
    command=save_file
    )
save_button.grid(row=1, column=0, padx=5)

save_as_button = ctk.CTkButton(
    master=frame_button,
    text="Save As",
    border_color="light blue",
    border_width=2,
    hover_color="blue",
    command=save_as_file
    )
save_as_button.grid(row=2, column=0, padx=5, pady=15)


root.mainloop()
