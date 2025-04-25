LIMITE_MAX_DE_VELOCIDADE = 110
LIMITE_MIN_DE_VELOCIDADE = 60
multa = 400 #% da velocidade do carro
carros = []

for i in range(3): 
    placa = input("Digite a placa do carro: ")
    velocidade = input("Digite a velocidade (km/h): ")

    carro = {
        "placa": placa,
        "velocidade": velocidade
    }

    carros.append(carro)

for carro in carros:
    print(f"Placa: {carro['placa']} - Velocidade: {carro['velocidade']} km/h")
