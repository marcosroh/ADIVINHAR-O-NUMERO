import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)  # Número secreto entre 1 e 100
    tentativas = 0
    adivinhou = False

    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Estou pensando em um número entre 1 e 100.")

    while not adivinhou:
        palpite = int(input("Faça o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            adivinhou = True
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")

if __name__ == "__main__":
    adivinhar_numero()
