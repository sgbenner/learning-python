import random
from tkinter import *
import pandas

## import word list
word_list_df = pandas.read_csv("data/word_list.csv")


# Functions
def next_word():
    word_row = random.randint(0, len(words_to_study) - 1)

    next_word = words_to_study[word_row]

    # set up new word
    word_label.config(text=next_word[0])
    definition_label.config(text="")

    # show definition
    definition_label.after(1000, lambda: definition_label.config(text=next_word[1]))


# Build UI

screen = Tk()
screen.title("Flash Card App")
screen.config(pady=20, padx=20)

#### initialize flash card app, ask user how many words to study
word_to_study_label = Label(text="How many words do you want to study?")
word_to_study_label.grid(column=0, row=0, columnspan=2)

words_to_study_entry = Entry()
words_to_study_entry.grid(column=0, row=1)

button_pressed = BooleanVar()

words_to_study_submit_button = Button(text="OK", command=lambda: button_pressed.set(True))
words_to_study_submit_button.grid(column=1, row=1)

# wait for button to be pressed:
words_to_study_submit_button.wait_variable(button_pressed)

if button_pressed.get():
    words_to_study = [(word, definition) for rank, word, definition in
                      zip(word_list_df["rank"], word_list_df["word"], word_list_df["definition"]) if
                      rank <= int(words_to_study_entry.get())]

    # build new UI with flashcards
    word_to_study_label.destroy()
    words_to_study_entry.destroy()
    words_to_study_submit_button.destroy()

    # Labels
    word_label = Label(text="")
    word_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    definition_label = Label(text="")
    definition_label.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

    # Right/Wrong Buttons
    # correct_button_image = PhotoImage(file="")
    correct_button = Button(text="Correct", command=next_word, highlightthickness=0)
    correct_button.grid(column=0, row=2)

    wrong_button = Button(text="Incorrect", command=next_word, highlightthickness=0)
    wrong_button.grid(column=1, row=2)

    next_word()

screen.mainloop()
