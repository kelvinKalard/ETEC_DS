# Importação dos recursos necessários da biblioteca colorama[cite: 1, 16]
from colorama import Fore, Style

# Lista para armazenar as mensagens referentes a cada nível do reservatório
mensagens_situacao = [
    "Muito baixo (crítico)", # Índice 0 -> Nível 1
    "Baixo",                 # Índice 1 -> Nível 2
    "Médio",                 # Índice 2 -> Nível 3
    "Alto",                  # Índice 3 -> Nível 4
    "Muito alto (alerta)"    # Índice 4 -> Nível 5
]

# Função responsável por definir a cor da mensagem conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED      # Vermelho[cite: 1, 16]
    elif nivel == 2:
        return Fore.YELLOW   # Amarelo[cite: 1, 16]
    elif nivel == 3:
        return Fore.GREEN    # Verde[cite: 1, 16]
    elif nivel == 4:
        return Fore.CYAN     # Ciano[cite: 1]
    elif nivel == 5:
        return Fore.BLUE     # Azul[cite: 1]
    else:
        return Style.RESET_ALL

# Simulação do ambiente de monitoramento (sem necessidade de entrada do usuário)[cite: 1]
niveis_simulados = [1, 2, 3, 4, 5] # Lista armazenando os níveis[cite: 1]

print("Iniciando simulação de monitoramento do reservatório...\n")

for nivel in niveis_simulados:
    # Chama a função para resgatar a cor correspondente ao nível[cite: 1]
    cor = definir_cor(nivel)
    
    # Busca a mensagem na lista. Subtrai-se 1 porque os índices das listas em Python começam em 0[cite: 10]
    mensagem = mensagens_situacao[nivel - 1]
    
    # Exibe no terminal a situação atual do reservatório com a cor correspondente[cite: 1, 16]
    print(cor + f"Nível {nivel}: {mensagem}")

# Restaura o estilo padrão do terminal após a exibição das mensagens para evitar que a cor vaze para outros comandos[cite: 1, 16]
print(Style.RESET_ALL)