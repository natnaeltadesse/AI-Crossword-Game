import tkinter as tk
from tkinter import messagebox
def clue_list_to_dict(word_list, clue_list):
    return {word_list[i]: clue_list[i] for i in range(len(word_list))}
 # Constants for the crossword grid size and the possible words
GRID_SIZE = 8
WORD_LIST = ['dog', 'cat', 'bird', 'fish', 'lion', 'tiger', 'owl', 'rat', 'bat', 'cow', 'duck', 'goose', 'frog', 'pig',
             'ant', 'bee', 'hen', 'fox', 'ram']
CLUE_LIST = clue_list_to_dict(WORD_LIST, ['A pet that barks', 'A pet that meows', 'A creature that flies',
             'An aquatic animal', 'The king of the jungle', 'A large carnivore with stripes',
             'A nocturnal bird', 'A small rodent', 'A flying mammal',
             'A farm animal that gives milk', 'A bird that quacks', 'A large waterbird',
             'An amphibian that jumps', 'A farm animal that oinks', 'A tiny insect',
             'An insect that makes honey', 'A female bird that lays eggs',
             'A cunning, small carnivore', 'A male sheep'])
grid = [['#' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
clue_labels = []
 # Function to update a square in the grid
def update_grid(row, col, text_var):
    value = text_var.lower()
    grid[row][col] = value
    if value == '':
        value = '#'
    text = '      ' + value + '      '
    labels[row][col].config(text=text)
 # Function to handle submission of a word
def submit_word():
    word = word_var.get().lower()
    if word not in WORD_LIST:
        messagebox.showerror('Error', 'The word is not in the list.')
        return
    direction = direction_var.get()
    row = int(row_var.get()) - 1
    col = int(col_var.get()) - 1
    if direction == 'across':
        if col + len(word) > GRID_SIZE:
            messagebox.showerror('Error', 'The word does not fit.')
            return
        for i in range(len(word)):
            if grid[row][col + i] != '#' and grid[row][col + i] != word[i]:
                messagebox.showerror('Error', 'The word conflicts with an existing letter.')
                return
        # Fill in the word horizontally in the grid
        for i in range(len(word)):
            update_grid(row, col + i, word[i])
    elif direction == 'down':
        if row + len(word) > GRID_SIZE:
            messagebox.showerror('Error', 'The word does not fit.')
            return
        for i in range(len(word)):
            if grid[row + i][col] != '#' and grid[row + i][col] != word[i]:
                messagebox.showerror('Error', 'The word conflicts with an existing letter.')
                return
        # Fill in the word vertically in the grid
        for i in range(len(word)):
            update_grid(row + i, col, word[i])
     # Make the corresponding clue label's background green
    for lbl in clue_labels:
        if lbl["text"].split(". ")[1] == CLUE_LIST[word]:
            lbl.config(bg="green")
     # Clear the entry fields after successful submission
    word_var.set('')
    direction_var.set('')
    row_var.set('')
    col_var.set('')
 # Create the Tkinter GUI
root = tk.Tk()
root.title('Crossword Game')
# Create the crossword grid using labels
labels = []
square_vars = []
for i in range(GRID_SIZE):
    row = []
    var_row = []
    for j in range(GRID_SIZE):
        var = tk.StringVar()
        var.trace('w', lambda *args, row=i, col=j, var=var: update_grid(row, col, var))
        var_row.append(var)
        label = tk.Label(root, text='                  #                    ')
        label.grid(row=i + 1, column=j)
        row.append(label)
    labels.append(row)
    square_vars.append(var_row)
# Create the clue labels
clue_label = tk.Label(root, text='Clues:', font=('Arial', 14, 'bold'))
clue_label.grid(row=0, column=GRID_SIZE + 1)
clue_number = 1
for word, clue in CLUE_LIST.items():
    label = tk.Label(root, text=f'{clue_number}. {clue}')
    label.grid(row=clue_number, column=GRID_SIZE + 1)
    clue_labels.append(label)
    clue_number += 1
# Create the word submission fields
word_label = tk.Label(root, text='Word:', font=('Arial', 12))
word_label.grid(row=GRID_SIZE + 2, column=0)
word_var = tk.StringVar()
word_entry = tk.Entry(root, textvariable=word_var)
word_entry.grid(row=GRID_SIZE + 2, column=1)
direction_label = tk.Label(root, text='Direction:', font=('Arial', 12))
direction_label.grid(row=GRID_SIZE + 3, column=0)
direction_var = tk.StringVar()
direction_entry = tk.Entry(root, textvariable=direction_var)
direction_entry.grid(row=GRID_SIZE + 3, column=1)
row_label = tk.Label(root, text='Row:', font=('Arial', 12))
row_label.grid(row=GRID_SIZE + 4, column=0)
row_var = tk.StringVar()
row_entry = tk.Entry(root, textvariable=row_var)
row_entry.grid(row=GRID_SIZE + 4, column=1)
col_label = tk.Label(root, text='Column:', font=('Arial', 12))
col_label.grid(row=GRID_SIZE + 5, column=0)
col_var = tk.StringVar()
col_entry = tk.Entry(root, textvariable=col_var)
col_entry.grid(row=GRID_SIZE + 5, column=1)
submit_button = tk.Button(root, text='Submit', command=submit_word)
submit_button.grid(row=GRID_SIZE + 6, column=1)
# Start the GUI mainloop
root.mainloop()
