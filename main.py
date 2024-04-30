from tkinter import Tk, Label, Button, Entry, Toplevel, messagebox

def submit_story1_entries(entries, tl):
    # Extracting the input from entry fields
    name = entries['name'].get()
    adjective1 = entries['adjective1'].get()
    noun1 = entries['noun1'].get()
    verb1 = entries['verb1'].get()
    noun2 = entries['noun2'].get()
    verb2 = entries['verb2'].get()
    adjective2 = entries['adjective2'].get()

    # Generate the story using the inputs
    story = f'''
        Once upon a time in a quaint little village, there lived a {adjective1} {noun1} named {name}. {name} was known for their insatiable curiosity and boundless energy. Every morning, they would {verb1} out of bed, eager to explore the world beyond their doorstep.

One sunny day, {name} discovered an ancient map hidden in the attic. The map depicted a mysterious island called “Zephyr Isle,” rumored to hold a treasure more valuable than all the gold in the world. Without hesitation, {name} packed their {noun2}, donned a wide-brimmed hat, and set sail on a rickety old boat.

The journey was anything but smooth. Storms {verb2} the tiny vessel, and {name} clung to the mast, their heart pounding with equal parts fear and excitement. As the waves subsided, Zephyr Isle emerged on the horizon—a lush paradise with {adjective2} palm trees, sparkling waterfalls, and colorful parrots that chattered like old friends.

{name} explored the island, following the map’s cryptic clues. They climbed jagged cliffs, crossed treacherous bridges, and even encountered a mischievous monkey who stole their hat. But {name} pressed on, driven by the promise of hidden riches.

At last, beneath a gnarled tree, {name} unearthed the treasure—a chest filled not with gold, but with something far more precious: a collection of handwritten letters. Each letter told a different story—a sailor’s longing for home, a lost love rekindled, a secret recipe for the world’s best chocolate chip cookies.

As {name} sat there, reading the heartfelt words, they realized that the true treasure was not material wealth but the connections forged through time and distance. And so, {name} decided to share these letters with the world, creating a cozy café where people could sip coffee, nibble on cookies, and read stories that spanned centuries.

And thus, “The Curious Café” was born, with {name} as its proud owner. Visitors came from far and wide, drawn by the enchanting tales and the aroma of freshly brewed coffee. And every evening, as the sun dipped below the horizon, {name} would sit by the window, watching the stars twinkle, knowing that they had found their own little piece of magic on Zephyr Isle.
'''

    # Display the generated story in a new message box or window
    messagebox.showinfo("Your Generated Story", story)
    tl.destroy()  # Close the input window after displaying the story

def Story1(win):
    # Creating a new window for inputs
    tl = Toplevel(win)
    tl.title("Input words for your story")
    tl.geometry("400x300")

    # Dictionary to hold the entry widgets
    entries = {}

    # Labels and entry fields for each part of speech
    labels = ['name', 'adjective1', 'noun1', 'verb1', 'noun2', 'verb2', 'adjective2']
    for idx, label in enumerate(labels):
        Label(tl, text=f"Enter a {label}:").place(x=10, y=30*idx + 10)
        entry = Entry(tl, width=25)
        entry.place(x=150, y=30*idx + 10)
        entries[label] = entry

    # Submit button
    Button(tl, text="Submit", command=lambda: submit_story1_entries(entries, tl)).place(x=150, y=30*len(labels) + 10)

# Main GUI setup
Screen = Tk()
Screen.title("Shepherd Automation Mad Libs Generator")
Screen.geometry("400x400")
Screen.config(bg="light blue")
Label(Screen, text="Shepherd Automation Mad Libs Generator").place(x=100, y=0)
Story1Button = Button(Screen, text='The Zephyr Isle Letters', font=("Times New Roman", 13), command=lambda: Story1(Screen))
Story1Button.place(x=10, y=30)

Screen.mainloop()
