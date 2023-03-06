# Solicita a entrada do usuário
entrada = input("Digite uma string para inverter: ")

# Inicializa a string de saída
saida = ""

# Itera de trás para frente pela string de entrada e adiciona cada caractere à string de saída
for i in range(len(entrada)-1, -1, -1):
    saida += entrada[i]

# Exibe a string de saída
print("String invertida:", saida)
