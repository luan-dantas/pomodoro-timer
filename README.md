# ⏰ Cronômetro Pomodoro em Python
Um simples e eficaz cronômetro Pomodoro desenvolvido em Python. Ele utiliza a biblioteca [tkinter](https://docs.python.org/3/library/tkinter.html) para a interface gráfica de usuário (GUI) e [plyer](https://pypi.org/project/plyer/) para as notificações nativas do sistema operacional (especialmente no Windows). Ideal para quem busca uma ferramenta minimalista para aplicar a técnica Pomodoro e **melhorar o foco e a produtividade**.

## ✨ Funcionalidades
* Ciclos de Trabalho (Pomodoro): 25 minutos de duração.
* Pausas Curtas: 5 minutos de descanso após cada ciclo de trabalho.
* Pausas Longas: 15 minutos de descanso concedidos a cada 4 ciclos Pomodoro completos.
* Notificações Visuais: Alertas no sistema (Windows) indicam o início e o fim de cada ciclo.
* Interface Intuitiva: Botões claros para Iniciar, Pausar e Resetar o cronômetro.
* Contador de Pomodoros: Acompanhe quantos ciclos você já completou.

## 🚀 Como Instalar e Rodar
Para colocar o cronômetro para funcionar no seu computador, siga os passos abaixo:

### Pré-requisitos
Certifique-se de ter o Python 3 (versão 3.6 ou superior é recomendada) instalado em sua máquina.

1. Clone o Repositório
Primeiro, clone este repositório para o seu computador usando o Git:
```
git clone https://github.com/seu-usuario/nome-do-seu-repositorio.git
cd nome-do-seu-repositorio
```
Observação: Lembre-se de substituir ´seu-usuario/nome-do-seu-repositorio´ pelo caminho correto do seu repositório no GitHub!

2. Crie e Ative um Ambiente Virtual (Altamente Recomendado)
Criar um ambiente virtual isola as dependências do seu projeto, evitando conflitos com outras instalações de Python.

No Windows (Prompt de Comando ou PowerShell):
```
python -m venv venv
venv\Scripts\activate
```
No macOS ou Linux (Terminal):
```
python3 -m venv venv
source venv/bin/activate
```
3. Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias para o projeto:
```
pip install plyer
```
4. Execute o Programa
Após instalar as dependências, você pode executar o cronômetro:
```
python pomodoro.py
```
## 👨‍💻 Como Usar
1. A janela do cronômetro aparecerá com "25:00" e o estado "Pomodoro".
2. Clique no botão "Iniciar" para começar o ciclo de trabalho.
3. Se precisar de uma pausa, clique em "Pausar". Clique novamente para retomar.
4. Quando um ciclo terminar, você receberá uma notificação, e o cronômetro passará automaticamente para o próximo estado (descanso curto, descanso longo ou um novo Pomodoro).
5. Clique em "Resetar" a qualquer momento para zerar o cronômetro e reiniciar os ciclos completados.

## 🤝 Contribuição
Contribuições são muito bem-vindas! Se você tem ideias para melhorias, encontrou um bug ou quer adicionar novas funcionalidades, sinta-se à vontade para:

* Abrir uma Issue para relatar um problema ou sugerir uma ideia.
* Criar um Pull Request com suas alterações.

📄 Licença
Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo LICENSE para mais detalhes.
