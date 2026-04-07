class Personagem:
    def __init__(self, nome="Herói", hp=100):
        self.nome = nome
        self._hp = hp  # atributo "privado"
        self.zumbi = False

    def receber_dano(self, dano):
        # validação (blindagem)
        if dano < 0:
            raise ValueError("O dano não pode ser negativo!")

        if self.zumbi:
            raise Exception("Personagem já é um zumbi, não pode receber mais dano!")

        # aplica dano
        self._hp -= dano

        # trava HP em zero
        if self._hp <= 0:
            self._hp = 0
            self.zumbi = True
            print(self.nome, "virou um zumbi!")

    def mostrar_status(self):
        print("\n====== STATUS ======")
        print("Nome:", self.nome)
        print("HP:", self._hp)
        print("Zumbi:", self.zumbi)
        print("====================\n")


# Programa principal
try:
    p1 = Personagem()

    print("=== VIDA INICIAL ===")
    p1.mostrar_status()

    dano = int(input("Digite o dano recebido: "))

    p1.receber_dano(dano)

    print("=== VIDA APÓS DANO ===")
    p1.mostrar_status()

except ValueError as e:
    print("Erro:", e)

except Exception as e:
    print("Erro:", e)

# A declaração de classes, realizada com a palavra-chave class, possibilita a representação de entidades do mundo real, como um personagem em um jogo.
# O método construtor __init__ é utilizado para inicializar os atributos do objeto quando ele é criado. 
# Além disso, o uso de atributos com prefixo de sublinhado, como _hp, representa uma forma de encapsulamento, restringindo o acesso direto aos dados internos da classe.
# O tratamento de exceções com o comando raise, que permite interromper a execução em casos de operações inválidas, como a inserção de valores negativos de dano. 
# Para que a vida do personagem não posso assumir valores negativos, foi criada uma validação que impede que o HP seja menor que zero.
# Além disso, foi implementada uma regra de negócio em que o personagem se transforma em zumbi ao atingir zero de vida, impedindo novas interações inválidas. Dessa forma, o sistema foi “blindado” contra erros comuns.