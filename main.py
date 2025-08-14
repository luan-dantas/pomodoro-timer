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

rotulo_timer = tk.Label(janela, text="25:00", font=("Helvetica", 48))
rotulo_timer.pack(pady=20)

rotulo_estado = tk.Label(janela, text="Estado: Pomodoro", font=("Helvetica", 14))
rotulo_estado.pack()

rotulo_pomodoros = tk.Label(janela, text="Pomodotos completos: 0", font=("Helvetica", 14))
rotulo_pomodoros.pack()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_iniciar_pausar = tk.Button(frame_botoes, text="Iniciar", command=iniciar_pausar)
botao_iniciar_pausar.pack(side=tk.LEFT, padx=5)

botao_resetar = tk.Button(frame_botoes, text="Resetar", command=resetar)
botao_resetar.pack(side=tk.LEFT, padx=5)

janela.mainloop()