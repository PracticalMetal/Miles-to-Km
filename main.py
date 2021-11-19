import tkinter
from typing import Text

# defining the screen
window=tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(height=200,width=200)

#defing the widgets
    # defing the input entry
input=tkinter.Entry(width=10)
input.grid(row=0,column=0,padx=(100,20))

    # defing labels
miles=tkinter.Label(text="Miles",font=(20)).grid(row=0,column=2,padx=30)
is_equal=tkinter.Label(text="is equal to",font=(20)).grid(row=1,column=0)
ans=tkinter.Label(text="0",font=(20))
ans.grid(row=1,column=1)
km=tkinter.Label(text="Km",font=(20)).grid(row=1,column=2)


    # defining button

def calc():
    miles=float(input.get())
    km=miles*1.6
    ans.config(text=f"{km}")

calculate=tkinter.Button(text="Calculate",command=calc).grid(row=2,column=1)














window.mainloop()