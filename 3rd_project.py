import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def new_file(event=None):
    text.delete(1.0, tk.END)

def open_file(event=None):
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File saved!")

# Line Numbers of this ..
def update_line_numbers(event=None):
    lines = text.get("1.0", "end-1c").split("\n")
    line_numbers.config(state='normal')
    line_numbers.delete("1.0", tk.END)
    
    for i in range(1, len(lines)+1):
        line_numbers.insert(tk.END, f"{i}\n")
    
    line_numbers.config(state='disabled')

# Status Bar 
def update_status(event=None):
    row, col = text.index(tk.INSERT).split(".")
    status_bar.config(text=f"Line: {row} | Column: {col}")

def find_text():
    find = simpledialog.askstring("Find", "Enter text:")
    text.tag_remove("highlight", "1.0", tk.END)
    
    if find:
        start = "1.0"
        while True:
            start = text.search(find, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(find)}c"
            text.tag_add("highlight", start, end)
            start = end
        
        text.tag_config("highlight", background="yellow")

#Window 
root = tk.Tk()
root.title("Mini VS Code 🧠")
root.geometry("900x600")

# Menu 
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Find", command=find_text)

#Layout
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Line numbers
line_numbers = tk.Text(frame, width=4, padx=5, takefocus=0, border=0,
                       background="lightgray", state='disabled')
line_numbers.pack(side=tk.LEFT, fill=tk.Y)

# Text area
text = tk.Text(frame, wrap=tk.NONE, font=("Consolas", 12))
text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#  Status Bar 
status_bar = tk.Label(root, text="Line: 1 | Column: 0", anchor="w")
status_bar.pack(fill=tk.X, side=tk.BOTTOM)

#  Events ..
text.bind("<KeyRelease>", update_line_numbers)
text.bind("<KeyRelease>", update_status)

# Shortcuts of ...
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-f>", lambda e: find_text())

# Run-
root.mainloop()
