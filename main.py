import tkinter as tk
from tkinter import messagebox
import time
from plyer import notification


pomodoro_tempo = 25 * 60  
descanso_curto_tempo = 5 * 60  
descanso_longo_tempo = 15 * 60 
tempo_restante = pomodoro_tempo
executando = False
pomodoros_completos = 0
estado_atual = "Pomodoro"

def atualizar_tempo():
    pass 

def iniciar_pausar():
    pass 

def resetar():
    pass

# Criando a janela principal
janela = tk.Tk()
janela.title("Cronômetro Pomodoro")
janela.geometry("400x250")
janela.resizable(False, False)

janela.mainloop()