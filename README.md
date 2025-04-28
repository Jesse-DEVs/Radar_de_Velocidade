Controle de Velocidade de Veículos 🚗💨
Este é um projeto simples em Python para controle de velocidade de veículos.
Ele permite cadastrar veículos com suas respectivas velocidades, verifica se estão dentro dos limites permitidos e gera um relatório com o status e o valor da multa (se houver).

📋 Funcionalidades
Adicionar veículos informando a placa e a velocidade.

Verificar se a velocidade está:

Acima do limite (multa proporcional).

Abaixo do limite (multa fixa).

Dentro do limite (sem multa).

Exibir um relatório completo de todos os veículos registrados.

Menu interativo para fácil navegação.

⚙️ Como Funciona
Limite máximo de velocidade: 110 km/h

Limite mínimo de velocidade: 60 km/h

Multa para velocidade acima do limite: 400% da diferença entre a velocidade registrada e o limite máximo.

Multa para velocidade abaixo do limite: R$ 40,00 (valor fixo).

Velocidade dentro dos limites: Sem multa.

🧩 Estrutura do Código
verificar_velocidade(placa, velocidade): Função que analisa a velocidade e retorna o status e valor da multa.

exibir_menu(): Exibe as opções de interação no terminal.

Loop principal (if __name__ == "__main__") para gerenciar a execução do programa.
