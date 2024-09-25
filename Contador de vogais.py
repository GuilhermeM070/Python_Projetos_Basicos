def conta_vogais(texto):
    # Conjunto de vogais
    vogais = set('aeiouAEIOU')  
    contador = 0  # Inicializando o contador

    # Iterando pelos caracteres da string
    for char in texto:
        if char in vogais:  # Verificando se o caractere é uma vogal
            contador += 1  # Incrementa o contador se for uma vogal
    
    return contador  # Retornando o número total de vogais

# Exemplo de uso
texto = input()
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")