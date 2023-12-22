from tkinter import *
import json


class Tarefa:
    

    def __init__(self, janela):
        self.janela = janela
        self.tarefas = []
        

        self.f1 = Frame(self.janela, width=600, height=300,bg='#F49536')
        self.f1.grid(row=0, column=0, sticky=NSEW)
        self.f2 = Frame(self.janela, width=600, height=100, bg='#272727')
        self.f2.grid(row=1, column=0, sticky=NSEW)

        self.lt = Listbox(self.f1, width=80, height=15, font=('arial', '10', 'bold'))
        self.lt.grid(row=1, column=1, padx=10, pady=20, sticky=NSEW, columnspan=1)
       
        self.entrada = Entry(self.f2,width=80, relief='flat',)
        self.entrada.focus_force()
        self.entrada.grid(row=1, column=1,padx= 50, pady= 10,columnspan=4, sticky=NSEW)
        
        self.b1 = Button(self.f2, text='Adicionar',relief='flat', command= self.adicionar )
        self.b1.grid(row=3, column=1,padx=10, pady= 20, sticky=NSEW, columnspan=1)

        self.b2 = Button(self.f2, text='Apagar', relief='flat', command= self.apagar)
        self.b2.grid(row=3, column=2,padx= 10, pady= 20, sticky=NSEW,columnspan=1)

        self.b3 = Button(self.f2, text='Listar', relief='flat', command= self.listar )
        self.b3.grid(row=3, column=3,padx= 10, pady= 20, sticky=NSEW,columnspan=1)

        self.b4 = Button(self.f2, text='Exibir', relief='flat', command= self.exibir)
        self.b4.grid(row=3, column=4,padx= 10, pady= 20, sticky=NSEW,columnspan=1)
    
    def adicionar(self):
        taref = self.entrada.get()
        self.lt.insert(END, taref)
        self.entrada.delete(0,END)

    def apagar(self):
        self.lt.delete(ACTIVE)

    def listar(self):
        self.lis = self.lt.get(0, END)
        with open('lista.json', 'w', encoding='UTF-8') as arquivo:
            json.dump(self.lis, arquivo, indent=4)

    def exibir(self):
        with open('lista.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        for i in dados:
            self.lt.insert(END, i)
       

inst = Tk()
inst.title('Gerenciado de tarefas')
Tarefa(inst)
inst.mainloop() 
