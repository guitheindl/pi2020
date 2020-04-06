class Dragao():

    def __init__(self, vida, elemento, ataque1, ataque2):
        self.vida = vida
        self.elemento = elemento
        self.ataque1 = ataque1
        self.ataque2 = ataque2

def critico(elementoA, elementoB):
    if elementoA == "agua" and elementoB == "fogo" or elementoB == "agua" and elementoA == "fogo":
        return True
    if elementoA == "terra" and elementoB == "fogo" or elementoB == "terra" and elementoA == "fogo":
        return True

    else:
        return False
        
dragao1 = Dragao(1000, 'fogo', 200, 300)
dragao2 = Dragao(1000, 'agua', 200, 300)

a = int(input("Qual dragão voce quer? 1 ou 2"))

if a == 1: 

    b = int(input("Qual ataque voce quer usar no inimigo? 1 ou 2"))

    if critico(dragao1.elemento, dragao2.elemento) is True:

        if b == 1:
            dragao1.ataque1 *= 2
            print(f"Voce tirou {dragao1.ataque1} de vida do adversário")
            vidadragao2 = dragao2.vida - dragao1.ataque1
            print(f"Ele ficou com {vidadragao2}")

        if b == 2:
            dragao1.ataque2 *= 2
            print(f"Voce tirou {dragao1.ataque2} de vida do adversário")
            vidadragao2 = dragao2.vida - dragao1.ataque2
            print(f"Ele ficou com {vidadragao2}")

    else:
        
        if b == 1:
            print(f"Voce tirou {dragao1.ataque1} de vida do adversário")
            vidadragao2 = dragao2.vida - dragao1.ataque1
            print(f"Ele ficou com {vidadragao2}")

        if b == 2:
            print(f"Voce tirou {dragao1.ataque2} de vida do adversário")
            vidadragao2 = dragao2.vida - dragao1.ataque2
            print(f"Ele ficou com {vidadragao2}")

if a == 2: 

    b = int(input("Qual ataque voce quer usar no inimigo? 1 ou 2"))

    if critico(dragao1.elemento, dragao2.elemento) is True:

        if b == 1:
            dragao2.ataque1 *= 2
            print(f"Voce tirou {dragao2.ataque1} de vida do adversário")
            vidadragao1 = dragao1.vida - dragao2.ataque1
            print(f"Ele ficou com {vidadragao1}")

        if b == 2:
            dragao2.ataque2 *= 2
            print(f"Voce tirou {dragao2.ataque2} de vida do adversário")
            vidadragao1 = dragao1.vida - dragao2.ataque2
            print(f"Ele ficou com {vidadragao1}")

    else:

        if b == 1:
            print(f"Voce tirou {dragao2.ataque1} de vida do adversário")
            vidadragao2 = dragao1.vida - dragao2.ataque1
            print(f"Ele ficou com {vidadragao1}")

        if b == 2:
            print(f"Voce tirou {dragao2.ataque2} de vida do adversário")
            vidadragao2 = dragao1.vida - dragao2.ataque2
            print(f"Ele ficou com {vidadragao1}")
