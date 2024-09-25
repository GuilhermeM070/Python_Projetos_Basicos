def verificar_numero_par_impar(numero):
  if numero % 2 == 0:
    return (f"Este numero é: Par ")
  else:
    return (f"Este numero é: Impar ")
  

numero = int(input("Escolha um numero, descobriremos se é Par ou Impar: "))

resultado = verificar_numero_par_impar(numero)

print(resultado)

