
from tkinter import *


#This part it's for create the window
window= Tk()
window.title("Calculator")

#Now we create de part where we show de result
i_text = Entry(window, font="arial 20")
i_text.grid( row=0, column=0, columnspan=4, padx=5, pady=5)

#Functions
i=0
def click_button(value):
    global i
    i_text.insert(i, value)
    i+=1

def delete():
    i_text.delete(0,END)
    i=0

def result():
    ecuation=i_text.get()
    result= eval(ecuation)
    i_text.delete(0,END)
    i_text.insert(0,result)
    i=0

#Buttons
butt1=Button(window, text="1", width=5, height=2, command= lambda: click_button(1))
butt2=Button(window, text="2", width=5, height=2, command= lambda: click_button(2))
butt3=Button(window, text="3", width=5, height=2, command= lambda: click_button(3))
butt4=Button(window, text="4", width=5, height=2, command= lambda: click_button(4))
butt5=Button(window, text="5", width=5, height=2, command= lambda: click_button(5))
butt6=Button(window, text="6", width=5, height=2, command= lambda: click_button(6))
butt7=Button(window, text="7", width=5, height=2, command= lambda: click_button(7))
butt8=Button(window, text="8", width=5, height=2, command= lambda: click_button(8))
butt9=Button(window, text="9", width=5, height=2, command= lambda: click_button(9))
butt0=Button(window, text="0", width=5, height=2, command= lambda: click_button(0))

butt_del=Button(window, text="AC", width=5, height=2, command= lambda: delete())
butt_par_op=Button(window, text="(", width=5, height=2, command= lambda: click_button("("))
butt_par_cl=Button(window, text=")", width=5, height=2, command= lambda: click_button(")"))
butt_dot=Button(window, text=".", width=5, height=2, command= lambda: click_button("."))

butt_div=Button(window, text="/", width=5, height=2, command= lambda: click_button("/"))
butt_mult=Button(window, text="*", width=5, height=2, command= lambda: click_button("*"))
butt_add=Button(window, text="+", width=5, height=2, command= lambda: click_button("+"))
butt_rest=Button(window, text="-", width=5, height=2, command= lambda: click_button("-"))
butt_result=Button(window, text="=", width=16, height=2, command= lambda: result())

#Position numbers
#1 row
butt_del.grid(row=1,column=2,padx=5,pady=5)
butt_par_op.grid(row=1,column=0,padx=5,pady=5)
butt_par_cl.grid(row=1,column=1,padx=5,pady=5)
butt_div.grid(row=1,column=3,padx=5,pady=5)
#2 row
butt7.grid(row=2,column=0,padx=5,pady=5)
butt8.grid(row=2,column=1,padx=5,pady=5)
butt9.grid(row=2,column=2,padx=5,pady=5)
butt_mult.grid(row=2,column=3,padx=5,pady=5)
#3 row
butt4.grid(row=3,column=0,padx=5,pady=5)
butt5.grid(row=3,column=1,padx=5,pady=5)
butt6.grid(row=3,column=2,padx=5,pady=5)
butt_add.grid(row=3,column=3,padx=5,pady=5)
#4 row
butt3.grid(row=4,column=2,padx=5,pady=5)
butt2.grid(row=4,column=1,padx=5,pady=5)
butt1.grid(row=4,column=0,padx=5,pady=5)
butt_rest.grid(row=4,column=3,padx=2,pady=2)
#5 row
butt0.grid(row=5,column=0, padx=5,pady=5)
butt_dot.grid(row=5,column=1,padx=5,pady=5)
butt_result.grid(row=5,column=2, columnspan=2, padx=5,pady=5)


window.mainloop()