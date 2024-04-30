import tkinter as tk
from tkinter import messagebox


def submit():
    # Collecting the text from the entries
    verbs = verbs_entry.get()
    nouns = nouns_entry.get()
    adjectives = adjectives_entry.get()

    # You could process these inputs further here
    # For now, let's just show them in a message box
    messagebox.showinfo(
        "Input Received",
        f"Verbs: {verbs}\nNouns: {nouns}\nAdjectives: {adjectives}")


# Creating the main window
root = tk.Tk()
root.title("Mad Libs Inputs")

# Setting the size of the window
root.geometry("300x200")

# Creating labels and text entry fields for verbs, nouns, and adjectives
tk.Label(root, text="Enter verbs:").pack()
verbs_entry = tk.Entry(root, width=25)
verbs_entry.pack()

tk.Label(root, text="Enter nouns:").pack()
nouns_entry = tk.Entry(root, width=25)
nouns_entry.pack()

tk.Label(root, text="Enter adjectives:").pack()
adjectives_entry = tk.Entry(root, width=25)
adjectives_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
