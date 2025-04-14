import tkinter as tk
from tkinter import messagebox

# Cria a janela principal
janela = tk.Tk()
janela.title("Kanban de Tarefas")

# Define cores de fundo e fonte
cor_fundo = "#F0F0F0"
fonte = ("ARIAL", 12)

# Cria um quadro principal para os quadros Kanban
quadro_principal = tk.Frame(janela, bg=cor_fundo)
quadro_principal.pack()

# Cria quadros para representar os estágios Kanban
quadro_a_fazer = tk.Frame(quadro_principal,borderwidth=2, relief=tk.SOLID)
quadro_a_fazer.pack(side=tk.LEFT, padx=20)
quadro_em_progresso = tk.Frame(quadro_principal, borderwidth=3, relief=tk.SOLID)
quadro_em_progresso.pack(side=tk.LEFT, padx=20)
quadro_concluido = tk.Frame(quadro_principal, borderwidth=3, relief=tk.SOLID)
quadro_concluido.pack(side=tk.LEFT, padx=20)

# Define cores para os quadros Kanban e suas bordas
cor_a_fazer = "#ff0000" # VERMELHO
cor_em_progresso= "#FFFF00" # AMARELO
cor_concluido = "#98FB98" # VERDE


# Adiciona rótulos para identificação dos quadros Kanban
label_a_fazer = tk.Label(quadro_a_fazer, text="A fazer",width=26, height=3,font=fonte, bg=cor_a_fazer,borderwidth=2,relief=tk.SOLID)
label_a_fazer.pack()
label_em_progresso = tk.Label(quadro_em_progresso, text="Em progresso",width=26, height=3, font=fonte, bg=cor_em_progresso,borderwidth=2,relief=tk.SOLID)
label_em_progresso.pack()
label_concluido = tk.Label(quadro_concluido, text="Concluído",width=26, height=3, font=fonte, bg=cor_concluido,borderwidth=2,relief=tk.SOLID)
label_concluido.pack()

# Cria as listas em cada coluna
lista_a_fazer = tk.Listbox(quadro_a_fazer, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_a_fazer.pack()
lista_em_progresso = tk.Listbox(quadro_em_progresso, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_em_progresso.pack()
lista_concluido = tk.Listbox(quadro_concluido, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_concluido.pack()


# Cria um quadro para a entrada de texto e botão de adicionar
escrevaTarefa = tk.Label(text="Escreva abaixo a sua tarefa, após clique em 'Adicionar Tarefa' :",font=fonte)
escrevaTarefa.pack(pady=5)
quadro_superior = tk.Frame(janela, bg=cor_fundo)
quadro_superior.pack(pady=20)
entrada = tk.Entry(quadro_superior, width=40, font=fonte)
entrada.pack()


def adicionar_tarefa():

  nova_tarefa = entrada.get()
  if nova_tarefa:
    
    lista_a_fazer.insert(tk.END, nova_tarefa)
    entrada.delete(0, tk.END)

  else:
    messagebox.showwarning("Aviso", "Digite uma tarefa válida!")


btn_adicionar = tk.Button(quadro_superior, text="Adicionar Tarefa", command=adicionar_tarefa, font=fonte)
btn_adicionar.pack()

def mover_para_em_progresso():

  try:
    selecionada = lista_a_fazer.curselection()[0]
    tarefa = lista_a_fazer.get(selecionada)
    lista_a_fazer.delete(selecionada)
    lista_em_progresso.insert(tk.END, tarefa)

  except IndexError:

    messagebox.showwarning("Aviso", "Selecione uma tarefa para mover para 'Em progresso'!")

#Botão para mover tarefa A fazer para em progresso
btn_mover_em_progresso = tk.Button(quadro_a_fazer, text="Mover para 'Em progresso'\n>>>>>", width=25, height=3,borderwidth=2,relief=tk.SOLID, command=mover_para_em_progresso,font=fonte)
btn_mover_em_progresso.pack()

def mover_para_concluido():
  try:

    selecionada = lista_em_progresso.curselection()[0]
    tarefa = lista_em_progresso.get(selecionada)
    lista_em_progresso.delete(selecionada)
    lista_concluido.insert(tk.END, tarefa)
  except IndexError:

    messagebox.showwarning("Aviso", "Selecione uma tarefa para mover para 'Concluído'!")

#Botão para mover tarefa em progresso para concluido
btn_mover_concluido = tk.Button(quadro_em_progresso, text="Mover para 'Concluído'\n>>>>>", width=25, height=3,borderwidth=2,relief=tk.SOLID, command=mover_para_concluido, font=fonte)
btn_mover_concluido.pack()

def remover_tarefa():
  try:
    selecionada = lista_concluido.curselection()[0]
    lista_concluido.delete(selecionada)

  except IndexError:
    messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

#Botão para remover tarefa de concluido
btn_remover = tk.Button(quadro_concluido, text="Remover Tarefa", width=25, height=3,borderwidth=2,relief=tk.SOLID, command=remover_tarefa, font=fonte)
btn_remover.pack()

# Inicia a interface gráfica
janela.mainloop()