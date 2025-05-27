class Player:
    def __init__(self, nome):
    # contrutor da classe
        self.nome = nome
        self.energia = 100
        self.fome = 100
        self.higiene = 100
        self.mental = 100
        self.dinheiro = 50
        self.profissao = None

    # métodos(ações)
    def comer(self):
        if self.dinheiro < 10:
            return f"{self.nome} Não Tem Dinheiro Suficiente!"
        else:
            self.dinheiro -= 10
            self.fome = min(100, self.fome + 35)
    
    def tomar_banho(self):
        if self.dinheiro < 1.5:
            return f"{self.nome} Não Tem Dinheiro Suficiente!"
        else:
            self.higiene = min(100, self.higiene + 100)
            
            self.dinheiro -= 1.5
            return f"{self.nome} Está Cheiroso!"
    
    def dormir(self):
        if self.fome == 0 or self.fome < 0:
            self.fome = 0
            return f"{self.nome} Precisa Comer Urgentemente!"
        if self.higiene == 0 or self.higiene < 0:
            self.higiene = 0
            return f"{self.nome} Está Fedendo!"
        else:
            self.energia = min(100, self.energia + 40)
            self.mental = min(100, self.mental + 10)

            self.fome -= 5
            self.higiene -= 5

            if self.higiene == 0 or self.higiene < 0:
                self.higiene = 0
                return f"{self.nome} Precisa Tomar Banho!"
            if self.fome == 0 or self.fome < 0:
                self.fome = 0
                return f"{self.nome} Precisa Comer Urgentemente!"

    def trabalhar(self):
        if self.energia <= 40:
            return f"{self.nome} Está Muito Cansado!"
        if self.mental <= 15:
            return f"{self.nome} Não Quer Trabalhar!"
        if self.fome <= 25:
            return f"{self.nome} Precisa Comer!"
        if self.higiene <= 25:
            return f"{self.nome} Está Fedendo!"

        else:
            self.dinheiro += 80

            self.energia -= 20
            self.mental -= 15
            self.higiene -= 35
            self.fome -= 25

            if self.mental == 0 or self.mental < 0:
                self.mental = 0
                return f"{self.nome} Precisa Descansar/Relaxar, Estresse Muito Alto!"
            if self.higiene == 0 or self.higiene < 0:
                self.higiene = 0
                return f"{self.nome} Precisa Tomar Banho!"
            if self.fome == 0 or self.fome < 0:
                self.fome = 0
                return f"{self.nome} Precisa Comer Urgentemente!"
            if self.energia == 0 or self.energia < 0:
                self.energia = 0
                return f"{self.nome} Precisa Descansar!"
    
    def relaxar(self):
        if self.energia < 5:
            return f"{self.nome} Precisa Descansar!"
        if self.fome < 5:
            return f"{self.nome} Precisa Comer!"
        
        else:
            self.mental = min(100, self.mental + 50)

            self.energia -= 5
            self.higiene -= 5
            self.fome -= 5

            if self.fome == 0 or self.fome < 0:
                self.fome = 0
                return f"{self.nome} Precisa Comer Urgentemente!"
            if self.higiene == 0 or self.higiene < 0:
                self.higiene = 0
                return f"{self.nome} Está Fedendo!"
            if self.energia == 0 or self.energia < 0:
                self.energia = 0
                return f"{self.nome} Precisa Dormir!"
    
    def mostrar_status(self):
        return f'''
            👤{self.nome}
            🔋Energia: {self.energia}
            🍖Fome: {self.fome}
            🧼Higiene: {self.higiene}
            🧠Mental: {self.mental}
            🎭Profissão: {self.profissao}
            💰Dinheiro: {self.dinheiro} '''   

if __name__ == "__main__":
# criar um objeto para o player
    object1 = Player("Felipe")
