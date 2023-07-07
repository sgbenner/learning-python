import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label".title(), font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)  # place it on the screen
my_label["text"] = "Label Text".title()


# Button
def button_clicked():
    txt_input = input.get()
    my_label.config(text=txt_input)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
button2 = tkinter.Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry (input)
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
