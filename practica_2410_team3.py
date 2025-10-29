"""
SESION NRO 3 - 24-10-2025
 mandreamarcos@hotmail.com
 tomasdeleeuw2007@gmail.com
 melodyalexandralanza@gmail.com
 ggbarrios.87@gmail.com
 odellsilva300@gmail.com
"""""

numero = 1 #Cualquier nro mayor a 0, entero positivo para que entre al While


while numero != 0 and numero > 0:
    factorial = 1
    print('*****************************************')
    num = input('Ingrese un número entero positivo: ')
    
    if num.isdigit():
        numero = int(num)
    else:
        break ## si ingresa una letra o un float corta el programa
 
    if int(numero) != numero: #Si no es entero corte el ciclo
        break

    if  numero != 0 and numero > 0: #Continua evaluanddo Si es distinto de CERO y positivo
        
        palabra = input('Ingrese una palabra o frase: ')
        cant_caracteres = len(palabra)
        print(f'La cantidad de letras de su frase es: {cant_caracteres}\n')

        if cant_caracteres < 1:
            cant_caracteres = 1
        
        for i in range(1, cant_caracteres+1):
            factorial *= i

        print(f'El factorial de la cantidad de caracteres ingresados es {factorial}\n')
        calculo_valor = factorial % 2
        
        if calculo_valor == 0:
            print('El factorial del numero ingresado es par\n')
        else:
            print('El factorial del numero ingresado es impar\n')

    else:
        break #Termina si ingreso un CERO o un numero negativo



