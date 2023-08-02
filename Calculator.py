#Made by Aditya Anurag
  
from tkinter import * 
  
def click(event): 
     global scvalue 
     text = event.widget.cget("text") 
     print(text) 
     if text == "=": 
         if scvalue.get().isdigit(): 
             value = int(scvalue.get())     
         else: 
             value = eval(screen.get())     
         scvalue.set(value) 
         screen.update()      
     elif text == "C": 
         scvalue.set("") 
         screen.update() 
     else: 
         scvalue.set(scvalue.get()+text) 
         screen.update() 
          
  
root = Tk() 
root.geometry("300x500")  
root.title("Calculator By Aditya") 
  
scvalue = StringVar() 
scvalue.set("") 
screen = Entry(root,textvar =scvalue,font="lucida 35 bold") 
screen.pack(fill=X,padx=10,pady=10,ipadx=10) 
  
f = Frame(root,bg="grey") 
b = Button(f,text="9",bg ="orange", width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=0,column =0) 
b = Button(f,text="8",bg ="yellow",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=0,column =1) 
b = Button(f,text="7",bg ="aqua",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=0,column =2) 
b = Button(f,text="6",bg ="violet",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=0,column =3) 
b = Button(f,text="5",bg ="gold",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=1,column =0) 
b = Button(f,text="4",bg="red",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=1,column =1) 
b = Button(f,text="3",bg ="aquamarine",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=1,column =2) 
b = Button(f,text="2",bg ="orange",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=1,column =3)
b = Button(f,text="1",bg ="tan",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=2,column =0) 
b = Button(f,text="0",bg ="chocolate",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=2,column =1) 
b = Button(f,text=".",bg ="chartreuse",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=2,column =2) 
b = Button(f,text="C",bg ="blueviolet",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=2,column =3) 
b = Button(f,text="+",bg ="aliceblue",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=3,column =0) 
b = Button(f,text="-",bg ="azure",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=3,column =1) 
b = Button(f,text="*",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=3,column =2) 
b = Button(f,text="=",bg ="cornflowerblue",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=3,column =3) 
b = Button(f,text="/",bg ="teal",width= 2,height=1,font= "lucida 35 bold") 
b.bind("<Button-1>",click) 
b.grid(row=3,column =1) 
f.pack() 
  
root.mainloop()

