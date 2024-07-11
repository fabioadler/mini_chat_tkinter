from tkinter import *
from tkinter.ttk import *

class App():
    def __init__(self):
        self.tela = Tk()
        self.tela.iconbitmap("./img/5962463.ico")
        self.tela.title("Chat")
        self.tela.geometry("500x300")
        self.tela.resizable(False,False)
        self.layout()
        self.tela.mainloop()
    def envi(self):
        self.listTree.insert("",END,values=["eu",self.entrada1.get()])
    def layout(self):
        self.frame1 = Frame(self.tela)
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=0.9)
        self.listTree = Treeview(self.frame1,columns=("c1","c2"))
        self.listTree.heading("#0",text="")
        self.listTree.heading("#1",text="user")
        self.listTree.heading("#2",text="msg")
        self.listTree.column("#0",width=1)
        self.listTree.column("#1",width=100)
        self.listTree.column("#2",width=200)
        self.listTree.place(relx=0,rely=0,relwidth=0.97,relheight=1)
        self.scroll = Scrollbar(self.frame1,orient="vertical")
        self.listTree.configure(yscrollcommand=self.scroll.set)
        self.scroll.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        self.entrada1 = Entry(self.tela)
        self.entrada1.place(relx=0,rely=0.9,relwidth=0.9,relheight=0.1)
        self.bt1 = Button(self.tela,text="Env.",command=self.envi)
        self.bt1.place(relx=0.9,rely=0.9,relwidth=0.1,relheight=0.1)

App()