#coding:utf-8
import tkinter as tk

class Ball:
    def __init__(self,x,y,dx,dy,color):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.color=color

    def move(self,canvas):
        canvas.create_oval(self.x-20,self.y-20,self.x+20,self.y+20,
fill="white",width=0)
        self.x=self.x+self.dx
        self.y=self.y+self.dy

        canvas.create_oval(self.x-20,self.y-20,self.x+20,self.y+20,
fill=self.color,width=0)

        if self.x>=canvas.winfo_width():
            self.dx=-1
        if self.x<=0:
            self.dx=1
        if self.y>canvas.winfo_height():
            self.dy=-1
        if self.y<=0:
            self.dy=1

b=Ball(400,300,1,1,"red")

def loop():
    b.move(canvas)
    root.after(10,loop)

root=tk.Tk()
root.geometry("800x600")

canvas=tk.Canvas(root,width=800,height=600,bg="white")
canvas.place(x=0,y=0)

root.after(10,loop)

root.mainloop()
                        
