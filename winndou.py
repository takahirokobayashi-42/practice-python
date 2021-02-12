#coding:utf-8
import tkinter as tk

x=300
y=200


def event():
    global x,y
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="white",width=0)
    x=x+(1)
    y=y+(1)
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red")
    root.after(10,event)
    
root=tk.Tk()
root.geometry("600x400")

canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

root.after(10,event)

root.mainloop()
