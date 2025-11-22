import random

p = []   # array di partecipanti che varia
p2 = []  # array di partecipanti (fisso)

def main(num):
    for i in range(num):
        print(i+1, end="")
        nome = input("° participant: ")
        p.append(nome)
        p2.append(nome)

def estrazione(p, p2, num):
    i = 0
    while i < num:
        # Ultimi 2 partecipanti: caso speciale
        if i == num - 2:
            possibili = [x for x in p if x != p2[i]]
            if not possibili:
                return False

            estratto = random.choice(possibili)
            p.remove(estratto)

            possibili2 = [x for x in p if x != p2[i+1]]
            if not possibili2:
                return False

            estratto2 = random.choice(possibili2)

            with open(p2[i] + ".txt", "w") as file:
                file.write(estratto)
            with open(p2[i+1] + ".txt", "w") as file:
                file.write(estratto2)

            return True

        # Estrazione normale
        possibili = [x for x in p if x != p2[i]]
        if not possibili:
            return False

        estratto = random.choice(possibili)

        with open(p2[i] + ".txt", "w") as file:
            file.write(estratto)

        p.remove(estratto)
        i += 1

    return True


num = int(input("How many participants? "))

main(num)

while not estrazione(p, p2, num):
    # resetta e riprova
    p = p2[:]
print("Completed")
