from tkinter import Tk, Label, Button, Entry, Toplevel, Text, Scrollbar, VERTICAL, END


def submit_story1_entries(entries, win):
    # Extracting the input from entry fields
    win.geometry("500x800")
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

    # Clear existing widgets from the window
    for widget in win.winfo_children():
        widget.destroy()

    # Creating a scrollable Text widget to display the story
    text_area = Text(win, wrap='word', height=20, width=50)
    scrollbar = Scrollbar(win, command=text_area.yview, orient=VERTICAL)
    text_area.configure(yscrollcommand=scrollbar.set)

    text_area.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    Button(
        win,
        text="Restart",
        command=lambda: main_menu(win)).grid(
        row=1,
        column=0,
        sticky='nsew')
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # Insert the story into the text area and disable editing
    text_area.insert(END, story)
    text_area.config(state='disabled')


def submit_story2_entries(entries, win):
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
        Once upon a time, there was a {adjective1} {noun1} named {name}. {name} had always dreamed of {verb1} and exploring new {noun2}. One day, {name} stumbled upon a magical {noun2} that transported them to a {adjective2} world filled with wonders and adventures.

    In this new world, {name} encountered mythical creatures, solved puzzles, and discovered hidden treasures. They made friends with talking animals and helped restore peace to the land. {name} became a hero and was celebrated by the people of the kingdom.

    After their incredible journey, {name} returned home with a heart full of memories and a newfound sense of bravery. They realized that the real magic was not in the enchanted world, but within themselves.

    And so, {name} continued to {verb2} and explore, knowing that every day held the potential for a new and exciting adventure.
    '''

    # Clear existing widgets from the window
    for widget in win.winfo_children():
        widget.destroy()

    # Creating a scrollable Text widget to display the story
    text_area = Text(win, wrap='word', height=20, width=50)
    scrollbar = Scrollbar(win, command=text_area.yview, orient=VERTICAL)
    text_area.configure(yscrollcommand=scrollbar.set)

    text_area.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    Button(
        win,
        text="Restart",
        command=lambda: main_menu(win)).grid(
        row=1,
        column=0,
        sticky='nsew')
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # Insert the story into the text area and disable editing
    text_area.insert(END, story)
    text_area.config(state='disabled')


def Story2(win):
    # Creating a new window for inputs
    tl = Toplevel(win)
    tl.title("Input words for your story")
    tl.geometry("400x300")

    # Dictionary to hold the entry widgets
    entries = {}

    # Labels and entry fields for each part of speech
    labels = [
        'name',
        'adjective1',
        'noun1',
        'verb1',
        'noun2',
        'verb2',
        'adjective2']
    for idx, label in enumerate(labels):
        Label(tl, text=f"Enter a {label}:").place(x=10, y=30 * idx + 10)
        entry = Entry(tl, width=25)
        entry.place(x=150, y=30 * idx + 10)
        entries[label] = entry

    # Submit button
    Button(
        tl,
        text="Submit",
        command=lambda: submit_story2_entries(
            entries,
            win)).place(
        x=150,
        y=30 *
        len(labels) +
        10)


def submit_story3_entries(entries, win):
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
        In a land far away, there was a {adjective1} {noun1} named {name}. {name} had a special talent for {verb1} and was admired by everyone in the kingdom. One day, a {noun2} arrived with a message from the king.

    The king requested {name}'s help in solving a great mystery that had befallen the kingdom. {name} accepted the challenge and embarked on a thrilling quest to uncover the truth.

    During their journey, {name} encountered dangerous creatures, solved intricate puzzles, and faced their deepest fears. With each obstacle overcome, {name} grew stronger and wiser. Along the way, they made lifelong friends and discovered the power of teamwork.

    Finally, after many trials and tribulations, {name} discovered the hidden truth behind the mystery. They confronted the villain and restored peace to the kingdom. The king was grateful for {name}'s bravery and rewarded them with a {adjective2} treasure.

    {name} returned to their village as a hero, celebrated by the people for their courage and intelligence. They lived happily ever after, knowing that they had made a difference in the world.

    '''

    # Clear existing widgets from the window
    for widget in win.winfo_children():
        widget.destroy()

    # Creating a scrollable Text widget to display the story
    text_area = Text(win, wrap='word', height=20, width=50)
    scrollbar = Scrollbar(win, command=text_area.yview, orient=VERTICAL)
    text_area.configure(yscrollcommand=scrollbar.set)

    text_area.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')

    Button(
        win,
        text="Restart",
        command=lambda: main_menu(win)).grid(
        row=1,
        column=0,
        sticky='nsew')
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # Insert the story into the text area and disable editing
    text_area.insert(END, story)
    text_area.config(state='disabled')


def Story3(win):
    # Creating a new window for inputs
    tl = Toplevel(win)
    tl.title("Input words for your story")
    tl.geometry("400x300")

    # Dictionary to hold the entry widgets
    entries = {}

    # Labels and entry fields for each part of speech
    labels = [
        'name',
        'adjective1',
        'noun1',
        'verb1',
        'noun2',
        'verb2',
        'adjective2']
    for idx, label in enumerate(labels):
        Label(tl, text=f"Enter a {label}:").place(x=10, y=30 * idx + 10)
        entry = Entry(tl, width=25)
        entry.place(x=150, y=30 * idx + 10)
        entries[label] = entry

    # Submit button
    Button(
        tl,
        text="Submit",
        command=lambda: submit_story3_entries(
            entries,
            win)).place(
        x=150,
        y=30 *
        len(labels) +
        10)


def Story1(win):
    # Creating a new window for inputs
    tl = Toplevel(win)
    tl.title("Input words for your story")
    tl.geometry("400x300")

    # Dictionary to hold the entry widgets
    entries = {}

    # Labels and entry fields for each part of speech
    labels = [
        'name',
        'adjective1',
        'noun1',
        'verb1',
        'noun2',
        'verb2',
        'adjective2']
    for idx, label in enumerate(labels):
        Label(tl, text=f"Enter a {label}:").place(x=10, y=30 * idx + 10)
        entry = Entry(tl, width=25)
        entry.place(x=150, y=30 * idx + 10)
        entries[label] = entry

    # Submit button
    Button(
        tl,
        text="Submit",
        command=lambda: submit_story1_entries(
            entries,
            win)).place(
        x=150,
        y=30 *
        len(labels) +
        10)


def main_menu(win):
    win.geometry("350x150")
    for widget in win.winfo_children():
        widget.destroy()
    Label(win, text="Shepherd Automation Mad Libs Generator").place(x=0, y=0)
    Story1Button = Button(
        win,
        text='The Zeypher Island Letters',
        font=(
            "Times New Roman",
            13),
        command=lambda: Story1(win))
    Story1Button.place(x=10, y=30)
    Story2Button = Button(win, text='The Mysterious Quest', font=(
        "Times New Roman", 13), command=lambda: Story2(win))
    Story2Button.place(x=10, y=70)
    Story3Button = Button(win, text='The Heroic Journey', font=(
        "Times New Roman", 13), command=lambda: Story3(win))
    Story3Button.place(x=10, y=110)


# Main GUI setup
Screen = Tk()
Screen.title("Shepherd Automation Mad Libs Generator")
Screen.geometry("350x150")  # Adjusted size to better accommodate the text area
main_menu(Screen)
Screen.config(bg="light blue")
Label(Screen, text="Shepherd Automation Mad Libs Generator").place(x=100, y=0)
Screen.mainloop()