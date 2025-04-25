velocidade = 110
carro = float(input("Qual é a velocidade do carro? "))
multa = float(8.50)
velox = (carro - velocidade) * multa
if carro > velocidade:
    print(f"Você ultrapassou o limite de velocidade {velocidade} km/h e foi multado em {velox:.2f} reais")


