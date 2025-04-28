LIMITE_MAX_DE_VELOCIDADE = 110
LIMITE_MIN_DE_VELOCIDADE = 60
multa = 400  # % da velocidade do carro
carros = []

def verificar_velocidade(placa, velocidade):
    if velocidade > LIMITE_MAX_DE_VELOCIDADE:
        valor_multa = (velocidade - LIMITE_MAX_DE_VELOCIDADE) * multa / 100
        return {
            "placa": placa,
            "status": "acima do limite",
            "multa": round(valor_multa, 2)
        }
    elif velocidade < LIMITE_MIN_DE_VELOCIDADE:
        return {
            "placa": placa,
            "status": "abaixo do limite",
            "multa": 0
        }
    else:
        return {
            "placa": placa,
            "status": "dentro do limite",
            "multa": 0
        }

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Adicionar veículo")
    print("2. Exibir relatório de veículos")
    print("3. Sair")
    print("-------------")

if __name__ == "__main__":

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa do veículo: ")
            velocidade = float(input("Digite a velocidade do veículo: "))
            carros.append(verificar_velocidade(placa, velocidade))
            print("Veículo adicionado com sucesso!")
        elif opcao == "2":
            print("\nRelatório de Veículos:")
            for carro in carros:
                print(f"Placa: {carro['placa']}, Status: {carro['status']}, Multa: R$ {carro['multa']:.2f}")
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
