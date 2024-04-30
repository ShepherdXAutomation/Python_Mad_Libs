from tkinter import Tk, Label, Button

Screen = Tk()
Screen.title("Shepherd Automation Mad Libs Generator")
Screen.geometry("400x400")
Screen.config(bg="light blue")
Label(Screen, text="Shepherd Automation Mad Libs Generator").place(x=100, y=0)
Story1Button = Button(Screen, text='The Quest for the Ultimate Snack', font=("Times New Roman", 13), command=lambda: Story2(Screen), bg='Blue')
Story1Button.place(x=140,y=90)
Storry2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13), command=lambda: Story2(Screen), bg='Blue')
Storry2Button.place(x=150,y=150)

def Story1(win):
    def final(tl: Toplevel, name, adjective1, noun1, verb1, noun2, verb2, adjective2):

        text = f'''
        Once upon a time in a quaint little village, there lived a [adjective1] [noun1] named [name]. [name] was known for their insatiable curiosity and boundless energy. Every morning, they would [verb1] out of bed, eager to explore the world beyond their doorstep.

One sunny day, [name] discovered an ancient map hidden in the attic. The map depicted a mysterious island called “Zephyr Isle,” rumored to hold a treasure more valuable than all the gold in the world. Without hesitation, [name] packed their [noun2], donned a wide-brimmed hat, and set sail on a rickety old boat.

The journey was anything but smooth. Storms [verb2] the tiny vessel, and [name] clung to the mast, their heart pounding with equal parts fear and excitement. As the waves subsided, Zephyr Isle emerged on the horizon—a lush paradise with [adjective2] palm trees, sparkling waterfalls, and colorful parrots that chattered like old friends.

[name] explored the island, following the map’s cryptic clues. They climbed jagged cliffs, crossed treacherous bridges, and even encountered a mischievous monkey who stole their hat. But [name] pressed on, driven by the promise of hidden riches.

At last, beneath a gnarled tree, [name] unearthed the treasure—a chest filled not with gold, but with something far more precious: a collection of handwritten letters. Each letter told a different story—a sailor’s longing for home, a lost love rekindled, a secret recipe for the world’s best chocolate chip cookies.

As [name] sat there, reading the heartfelt words, they realized that the true treasure was not material wealth but the connections forged through time and distance. And so, [name] decided to share these letters with the world, creating a cozy café where people could sip coffee, nibble on cookies, and read stories that spanned centuries.

And thus, “The Curious Café” was born, with [name] as its proud owner. Visitors came from far and wide, drawn by the enchanting tales and the aroma of freshly brewed coffee. And every evening, as the sun dipped below the horizon, [name] would sit by the window, watching the stars twinkle, knowing that they had found their own little piece of magic on Zephyr Isle.


Screen.update()
Screen.mainloop()

1. function that hasks user for the number of nouns, adjectives and verbs they want in the story. They are assigned to variables called noun1, verb1, ajective1, etc.and
    def create_noun_array(noun_count):
        noun_array = []
        for i in range(noun_count):
            #should update this code to take information in from Tkinter. Tkinter should display a new page for every noun, verb, adjective, etc.
            noun_array.append(input(f"Enter noun {i+1}: "))
        return noun_array
    def create_verb_array(verb_count):
        verb_array = []
        for i in range(verb_count):
            #should update this code to take information in from Tkinter. Tkinter should display a new page for every noun, verb, adjective, etc.
            verb_array.append(input(f"Enter verb {i+1}: "))
        return verb_array
    def create_adjective_array(adjective_count):
        adjective_array = []
        for i in range(adjective_count):
            #should update this code to take information in from Tkinter. Tkinter should display a new page for every noun, verb, adjective, etc.
            adjective_array.append(input(f"Enter adjective {i+1}: "))
        return adjective_array

2. Then we wrap these variables in an api request asking chat gpt to generate a story with those variables.
    
3. We take the return from chatgpt and input the variables to the story.
4. We then display the story. 
5. User can then choose to restart.
6. Create a node.js version. '''