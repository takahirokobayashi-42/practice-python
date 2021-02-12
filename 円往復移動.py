#coding:utf-8
import tkinter as tk

x=400
y=300

dx=1

def move():
    global x,y,dx
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="white",width=0)

    x=x+dx

    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width=0)

    if x>canvas.winfo_width():
        dx=-1
    if x<=0:
        dx=1
    root.after(1,move)

root=tk.Tk()
root.geometry("600x400")

canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

root.after(1,move)

root.mainloop()
