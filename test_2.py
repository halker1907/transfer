import tkinter

window = tkinter.Tk()
checkbutton1_cheked = tkinter.StringVar()
checkbutton1 = tkinter.Checkbutton(window, text='существительное', onvalue='NOUN', variable=checkbutton1_cheked)
checkbutton1.pack()

checkbutton2_cheked = tkinter.StringVar()
checkbutton2 = tkinter.Checkbutton(window, text='глагол', onvalue='VERB', variable=checkbutton2_cheked)
checkbutton2.pack()

checkbutton3_cheked = tkinter.StringVar()
checkbutton3 = tkinter.Checkbutton(window, text='прилагательное', onvalue='ADJ', variable=checkbutton3_cheked)
checkbutton3.pack()


def run():
    pos = []
    if checkbutton1_cheked.get():
        pos.append(checkbutton1_cheked.get())

    elif checkbutton2_cheked.get():
        pos.append(checkbutton2_cheked.get())

    elif checkbutton3_cheked.get():
        pos.append(checkbutton3_cheked.get())
    print(pos)
    


button = tkinter.Button(window, command=run)
button.pack()
window.mainloop()