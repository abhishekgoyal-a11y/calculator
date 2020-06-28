from tkinter import *


root = Tk()
root.title("Calculator ")
root.geometry("165x280")
root.maxsize(170 ,280)
root.wm_iconbitmap("calculator.ico")


def click(event):
    text = event.widget.cget("text")
    if text == "C":
        scvalue.set("")
        screen.update()
    elif text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 15")
screen.pack(fill=X, pady=10)


# frame 1 starts
f = Frame(root, bg="grey")
b = Button(f, text="7", font="lucida 12 bold", padx=10, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="lucida 12 bold", padx=10, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="9", font="lucida 12 bold", padx=10, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="+", font="lucida 12 bold", padx=10, pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# frame 1 ends

# frame 2 starts
f = Frame(root, bg="grey")
b = Button(f, text="4", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="5", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="6", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="-", font="lucida 11 bold", padx=12.49, pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# frame 2 ends

# frame 3 starts
f = Frame(root, bg="grey")
b = Button(f, text="1", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="2", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="3", font="lucida 11 bold", padx=10.5, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="*", font="lucida 11 bold", padx=12.49, pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# frame 3 ends

# frame 4 starts
f = Frame(root, bg="grey")
b = Button(f, text="=", font="lucida 11 bold", padx=11, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="0", font="lucida 11 bold", padx=11, pady=10, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text=".", font="lucida 16 bold", padx=9, pady=5, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="/", font="lucida 11 bold", padx=11, pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# frame 4 ends

# frame 5 starts
f = Frame(root, bg="grey")
b = Button(f, text="Sin", font="Times 7 bold italic",
           padx=10, pady=7, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="Cos", font="Times 7 bold italic",
           padx=10, pady=7, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="Tan", font="Times 7 bold italic",
           padx=10, pady=7, bg="orange")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text="C", font="Times 12 bold italic", padx=10, pady=0)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# frame 5 ends

root.mainloop()
