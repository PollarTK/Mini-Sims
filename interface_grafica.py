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

        self.label_mensagem = tk.Label(root, text="", font=("Arial", 10))
        self.label_mensagem.pack()

    def atualizar_status(self):
        self.label_status.config(text=self.player.mostrar_status())

    # método que define a ação que acontece quando precionar o botao comer
    def botao_comer(self):
        mensagem = self.player.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
