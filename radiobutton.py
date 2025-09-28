from tkinter import*
win=Tk()
win.geometry('150x150')
lang=StringVar()
lang.set(' ')

def sho_choice():
    x=lang.get()
    win.configure(background=x)
    color1.configure(background=x)
    color2.configure(background=x)
    color3.configure(background=x)



color1=Radiobutton(win,text='red',variable=lang,value='red')
color1.pack()

color2=Radiobutton(win,text='blue',variable=lang,value='blue')
color2.pack()

color3=Radiobutton(win,text='pink',variable=lang,value='pink')
color3.pack()

btn_choice=Button(win,text='choice',command=sho_choice)
btn_choice.pack(pady=10)




win.mainloop()
