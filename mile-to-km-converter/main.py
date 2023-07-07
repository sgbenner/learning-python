from tkinter import *


## Functions
def calculate():
    input = float(entry_miles.get())
    km_result = input * 1.60934
    label_result.config(text=km_result)


window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_Km = Label(text="Km")
label_Km.grid(column=2, row=1)

label_equal_to = Label(text="is equal to")
label_equal_to.grid(column=0, row=1)

label_result = Label(text="0")
label_result.config(padx=20, pady=5)
label_result.grid(column=1, row=1)

# miles input
entry_miles = Entry()
entry_miles.focus()
entry_miles.config(width=5)
entry_miles.grid(column=1, row=0)

# Calculate Button
button_calc = Button(text="Calculate", command=calculate)
button_calc.grid(column=1, row=2)

window.mainloop()
