import tkinter as tk
from mini_sims import Player

class SimsApp:
    # construtor
    def __init__(self,root):
        # criando o player
        self.player = Player("Felipe")

        # titulo da janela
        root.title("Mini Sims")

        # tamanho da janela
        root.geometry("800x800")

        self.label_status = tk.Label(root, text=self.player.mostrar_status(),font=("Arial", 15),pady=10)
        self.label_status.pack()

        self.btn_comer = tk.Button(root, text="Comer", command=self.botao_comer)
        self.btn_comer.pack(pady = 5)
        
        self.btn_dormir = tk.Button(root, text="Dormir", command=self.botao_dormir)
        self.btn_dormir.pack(pady = 5)
        
        self.btn_relaxar = tk.Button(root, text="Relaxar", command=self.botao_relaxar)
        self.btn_relaxar.pack(pady = 5)
        
        self.btn_tomar_banho = tk.Button(root, text="Tomar Banho", command=self.botao_tomar_banho)
        self.btn_tomar_banho.pack(pady = 5)
        
        self.btn_trabalhar = tk.Button(root, text="Trabalhar", command=self.botao_trabalhar)
        self.btn_trabalhar.pack(pady = 5)

        self.label_mensagem = tk.Label(root, text="", font=("Arial", 10))
        self.label_mensagem.pack()

    def atualizar_status(self):
        self.label_status.config(text=self.player.mostrar_status())

    # método que define a ação que acontece quando precionar o botao comer
    def botao_comer(self):
        mensagem = self.player.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
        
    def botao_dormir(self):
        mensagem = self.player.dormir()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
        
    def botao_relaxar(self):
        mensagem = self.player.relaxar()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
        
    def botao_tomar_banho(self):
        mensagem = self.player.tomar_banho()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
    
    def botao_trabalhar(self):
        mensagem = self.player.trabalhar()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
