Primeiro_Numero = int(input("Digite o primeiro numero: "))
Segundo_Numero = int(input("Digite o segundo numero: "))

operador = input("Insira o operador artimético: ")

if operador == '+':
    resultado = Primeiro_Numero+Segundo_Numero
else:
    if operador == '-':
        resultado = Primeiro_Numero-Segundo_Numero
    else:
        if operador == '*':
            resultado = Primeiro_Numero*Segundo_Numero
        else:
            if operador == '/':
                resultado = Primeiro_Numero/Segundo_Numero
            
print ("O resultado:")
print(Primeiro_Numero ,'' ,operador , '' , Segundo_Numero,'= ',resultado)
