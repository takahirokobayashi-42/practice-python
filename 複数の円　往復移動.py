#coding:utf-8
import tkinter as tk

balls=[{"x":400,"y":300,"dx":10,"dy":10,"color":"red"},
       {"x":50,"y":100,"dx":-1,"dy":1,"color":"pink"},
       {"x":200,"y":100,"dx":-10,"dy":10,"color":"green"},
       {"x":100,"y":200,"dx":10,"dy":-10,"color":"blue"}]

def move():
    global balls
    for b in balls:
        canvas.create_oval(b["x"]-20,b["y"]-20,b["x"]+20,b["y"]+20,fill="white",width=0)

        b["x"]=b["x"]+b["dx"]
        b["y"]=b["y"]+b["dy"]


        canvas.create_oval(b["x"]-20,b["y"]-20,b["x"]+20,b["y"]+20,fill=b["color"],width=0)

        if b["x"]>=canvas.winfo_width():
            b["dx"]=-10
        if b["x"]<=0:
            b["dx"]=+10

        if b["y"]>=canvas.winfo_height():
            b["dy"]=-10

        if b["y"]<=0:
            b["dy"]=+10 
    root.after(70,move)



    
root=tk.Tk()
root.geometry("600x400")

canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

root.after(70,move)

root.mainloop()
