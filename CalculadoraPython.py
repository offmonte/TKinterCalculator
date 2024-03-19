from tkinter import *

app = Tk()
app.title('Calculadora Teste')
app.geometry('400x355')
app.minsize(400,355)
app.maxsize(400,355)

numero1 = ''
divisao = FALSE
multiplica = FALSE
subtrai = FALSE
soma = FALSE

app.configure(background='#282828')

e = Entry (app, width=15, borderwidth=4, relief=RAISED, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=2
)

#Função
def funcClick(num):
    e.insert(END, num)

def funcDividir():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def funcMultiplcar():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)

def funcSubtrair():
    global numero1
    global subtrai
    subtrai = TRUE
    numero1 = e.get()
    e.delete(0, END)

def funcSomar():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)

def funcClear():
    e.delete(0, END)

def funcResult():
    global divisao
    global soma
    global multiplica
    global subtrai
    numero2 = e.get()
    e.delete(0, END)
    if divisao == TRUE:
        e.insert(0,int(numero1) / int(numero2))
        divisao = FALSE
    if multiplica == TRUE:
        e.insert(0,int(numero1) * int(numero2))
        multiplica = FALSE
    if soma == TRUE:
        e.insert(0,int(numero1) + int(numero2))
        soma = FALSE
    if subtrai == TRUE:
        e.insert(0,int(numero1) - int(numero2))
        subtrai = FALSE


# Botão - Operadores
dividir = Button(app,
                text= '÷',
                padx=40,
                pady=20,
                command=funcDividir,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
dividir.grid(row=0, column=3)

#Primeria fileira
botao_1 =  Button(app,
            text= '1',
            padx=40,
            pady=20,
            command=lambda: funcClick(1),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_1.grid(row=1, column=0)

botao_2 =  Button(app,
            text= '2',
            padx=40,
            pady=20,
            command=lambda: funcClick(2),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_2.grid(row=1, column=1)

botao_3 =  Button(app,
            text= '3',
            padx=40,
            pady=20,
            command=lambda: funcClick(3),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_3.grid(row=1, column=2)

multiplicar = Button(app,
                text= '×',
                padx=40,
                pady=20,
                command=funcMultiplcar,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
multiplicar.grid(row=1, column=3)

#Segunda fileira

botao_4 =  Button(app,
            text= '4',
            padx=40,
            pady=20,
            command=lambda: funcClick(4),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_4.grid(row=2, column=0)

botao_5 =  Button(app,
            text= '5',
            padx=40,
            pady=20,
            command=lambda: funcClick(5),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_5.grid(row=2, column=1)

botao_6 =  Button(app,
            text= '6',
            padx=40,
            pady=20,
            command=lambda: funcClick(6),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_6.grid(row=2, column=2)

subtrair = Button(app,
                text= '-',
                padx=42,
                pady=20,
                command=funcSubtrair,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
subtrair.grid(row=2, column=3)

#terceira fileira

botao_7 =  Button(app,
            text= '7',
            padx=40,
            pady=20,
            command=lambda: funcClick(7),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_7.grid(row=3, column=0)

botao_8 =  Button(app,
            text= '8',
            padx=40,
            pady=20,
            command=lambda: funcClick(8),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_8.grid(row=3, column=1)

botao_9 =  Button(app,
            text= '9',
            padx=40,
            pady=20,
            command=lambda: funcClick(9),
            fg='#FFFFFF',
            activeforeground= '#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=RAISED,
            font=('futura', 12, 'bold')
            )
botao_9.grid(row=3, column=2)

somar = Button(app,
                text= '+',
                padx=40,
                pady=20,
                command=funcSomar,
                fg='#FFFFFF',
                activeforeground= '#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
somar.grid(row=3, column=3)
#quarta fileira
botao_0 = Button(app,
                text='0',
                padx=90,
                pady=20,
                command=lambda: funcClick(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
botao_0.grid(row=4, column=0, columnspan=2)  
clear = Button(app,
                text='C',
                padx=38.5,
                pady=20,
                command=funcClear,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
clear.grid(row=4, column=2)

result = Button(app,
                text='=',
                padx=40,
                pady=20,
                command=funcResult,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=RAISED,
                font=('futura', 12, 'bold')
                )
result.grid(row=4, column=3)  

app.mainloop()