# Sistema de Monitoramento de Velocidade de Veículos

Este é um sistema simples de monitoramento de velocidade de veículos. Ele permite adicionar veículos com suas respectivas placas e velocidades, verificar se estão dentro, acima ou abaixo do limite de velocidade e calcular a multa quando necessário.

## Descrição

O sistema possui as seguintes funcionalidades:
- Adicionar veículos, fornecendo a placa e a velocidade.
- Verificar a velocidade de cada veículo em relação ao limite de velocidade estabelecido.
- Exibir um relatório com as informações dos veículos, como placa, status (dentro do limite, acima ou abaixo do limite) e o valor da multa (se houver).
- Opção para sair do programa.

## Limites de Velocidade

- **Limite máximo de velocidade**: 110 km/h
- **Limite mínimo de velocidade**: 60 km/h

Se a velocidade do veículo for acima de 110 km/h, o sistema calculará uma multa proporcional à quantidade de km/h excedidos. A multa é definida como 400% do valor excedente da velocidade.

## Como usar

### Menu de opções:
1. **Adicionar veículo**: Permite inserir a placa e a velocidade de um veículo.
2. **Exibir relatório de veículos**: Exibe um relatório com a placa, status e a multa (se aplicável) de todos os veículos cadastrados.
3. **Sair**: Finaliza o programa.

### Exemplo de uso:
```python
Digite a placa do veículo: ABC1234
Digite a velocidade do veículo: 120
Veículo adicionado com sucesso!

Relatório de Veículos:
Placa: ABC1234, Status: acima do limite, Multa: R$ 40.00
