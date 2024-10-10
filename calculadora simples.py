# -*- coding: utf-8 -*-
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("530x420")
        self.entry = tk.Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Criando campo de exibição        
        self.display = tk.Entry(self.master, width=20, font=("Myriad Pro", 36), relief="sunken", bd=2)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Criando botões dos numeros
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 2
        col_val = 0
        for button in buttons:
            if button.isdigit() or button == '.':  # Verifica se o botão é um número ou um ponto

                tk.Button(self.master, text=button, width=5, font=("Myriad Pro", 24), padx=5, pady=5,
                        bg="gray",   #Define a cor do fundo cinza para numeros
                        fg="white",  #Define a cor do texto para branco para números
                        relief="ridge", #Cria um efeito na borda do botão para dar impressão de 3d
                        command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val, sticky="nsew")
            else:  #Se o botão for um operador
                tk.Button(self.master, text=button, width=5, font=("Myriad Pro", 24), padx=5, pady=5,
                        bg="gainsboro", #Define a cor do fundo "gainsboro" para operadores
                        fg="black",  #Define a cor preta para texto dos operadores
                        relief="ridge",
                        command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        #Criando os botões de operação especial
        operators = ['C', '±', '%', '⌫']
        row_val = 1
        for i, operator in enumerate(operators):
            #IF necessário pois o botão backspace tem o command como delete, diferente dos outros operadores
            if operators == '⌫':
                tk.Button(self.master, width=5, font=("Myriad Pro", 24), padx=5, pady=5, command=self.delete_last_char).grid(row=row_val, column=4, sticky="nsew")
            else:     
                tk.Button(self.master, text=operator, width=5, font=("Myriad Pro", 24), padx=5, pady=5, bg="light gray", relief="ridge", command=lambda operator=operator: self.click_operator(operator)).grid(row=row_val, column=i, sticky="nsew")
    #funcionamento do sistema após clicado o =        
    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.display.insert(tk.END, button)
            
    #funcionamento após clicado algum operador especial
    def click_operator(self, operator):
        if operator == 'C':
            self.display.delete(0, tk.END)
        elif operator == '±':
            self.display.insert(tk.END, '-')
        elif operator == '%':
            self.display.insert(tk.END, '/100')
        #Operação para funcionamento do botão Backspace
        elif operator == '⌫':         
                display_text = self.display.get()
                if display_text:  #Verifica se o campo de exibição não está vazio
                    self.display.delete(0, tk.END)  #Limpa todo o campo de exibição
                    self.display.insert(0, display_text[:-1])  #Insere o texto sem o último caracter no campo de exibição

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()