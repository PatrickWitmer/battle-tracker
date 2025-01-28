import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Battle Tracker")
root.geometry("500x800")

# Character list
characters = []
current_turn = 0  # Tracks whose turn it is


# Function to add a character
def add_character():
    name = name_entry.get()
    health = health_entry.get()
    mana = mana_entry.get()
    initiative = initiative_entry.get()

    if (
        not name
        or not health.isdigit()
        or not mana.isdigit()
        or not initiative.isdigit()
    ):
        messagebox.showerror("Error", "Please fill out all fields correctly!")
        return

    characters.append(
        {
            "name": name,
            "health": int(health),
            "mana": int(mana),
            "initiative": int(initiative),
        }
    )
    # Sort characters by initiative (highest first)
    characters.sort(key=lambda c: c["initiative"], reverse=True)
    update_character_list()
    name_entry.delete(0, tk.END)
    health_entry.delete(0, tk.END)
    mana_entry.delete(0, tk.END)
    initiative_entry.delete(0, tk.END)


# Function to update the character display
def update_character_list():
    listbox.delete(0, tk.END)
    for idx, char in enumerate(characters):
        turn_marker = " <-- Current Turn" if idx == current_turn else ""
        listbox.insert(
            tk.END,
            f"{char['name']} - HP: {char['health']}, MP: {char['mana']}, Init: {char['initiative']}{turn_marker}",
        )


# Function to move to the next turn
def next_turn():
    global current_turn
    if characters:
        current_turn = (current_turn + 1) % len(characters)
        update_character_list()


# Labels and input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

health_label = tk.Label(root, text="Health:")
health_label.pack()
health_entry = tk.Entry(root)
health_entry.pack()

mana_label = tk.Label(root, text="Mana:")
mana_label.pack()
mana_entry = tk.Entry(root)
mana_entry.pack()

initiative_label = tk.Label(root, text="Initiative:")
initiative_label.pack()
initiative_entry = tk.Entry(root)
initiative_entry.pack()

# Add character button
add_button = tk.Button(root, text="Add Character", command=add_character)
add_button.pack()

# Character list display
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack()

# Next turn button
next_turn_button = tk.Button(root, text="Next Turn", command=next_turn)
next_turn_button.pack()

# Run the main loop
root.mainloop()
