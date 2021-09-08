from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")

# add widgets to screen
miles_input = Entry()

miles_label = Label(text="Miles")
is_equal_label = Label(text="is equal to")
km_result_label = Label(text="0")
km_label = Label(text="km")

calculate_button= Button(text="calculate")



window.mainloop()
