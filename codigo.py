import random

print("*" * 30)
print("BEM VINDO AO JOGO DA VELHA")


def jogar(palavras):
    palavra = random.choice(palavras)
    letras_descoberta = ["_"] * len(palavra)
    letras_errada = []
    tentativas = 6

    while tentativas > 0:
        print(f"Palavra: {' '.join(letras_descoberta)}")
        print(f"Tentativas Restantes: {tentativas}")

        letra = input("Digite uma letra: ").lower()
        print("*" * 30)

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_errada:
            print(f"Você já tentou essa letra. Tente outra. {letras_errada}")

        else:
            if letra in palavra:
                print(f"Boa! A letra '{letra}' está na palavra.")

            if letra not in palavra:
                print(f"A letra '{letra}' não está na palavra.")
                letras_errada.append(letra)  # Adiciona à lista de letras erradas
                tentativas -= 1  # Diminui uma tentativa

            for i in range(len(palavra)):
                for l in palavra:
                    if l == letra and palavra[i] == letra:
                        letras_descoberta[i] = letra

        if "_" not in letras_descoberta:
            print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
            return "Resultado: Vitória!"

    print("\nVocê usou todas as suas tentativas!")

    chute = input("Qual é a palavra? ").lower()

    if chute == palavra:
        print(f"\nParabéns! Você acertou! A palavra era: {palavra}")
        return "Resultado: Vitória!"
    else:
        print(f"\nQue pena! Você errou. A palavra era: {palavra}")
        return "Resultado: Derrota!"


palavras = ['alemanha', 'espanha', 'canada', 'irlanda', 'noruega', 'inglaterra', 'jamaica', 'australia', 'japao',
            ' portugal', 'brasil']

print(jogar(palavras))