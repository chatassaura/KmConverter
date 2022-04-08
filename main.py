from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)
window.minsize(width=250, height=100)

input_miles = Entry()
input_miles.grid(column=1, row=0)
lbl_equal = Label(text="is equal to")
lbl_equal.grid(column=0, row=1)
lbl_total = Label(text='0')
lbl_total.grid(column=1, row=1)
lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2, row=0)
lbl_Km = Label(text="Km")
lbl_Km.grid(column=2, row=1)


def button_click():
    miles = int(input_miles.get())
    km_converted = miles * 1.609
    lbl_total.config(text=round(km_converted, 2))


btn_calc = Button(text="Calculate", command=button_click)
btn_calc.grid(column=1, row=2)

window.mainloop()
