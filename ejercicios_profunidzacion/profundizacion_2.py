# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''
opera =" "
resultado = 1
calculadora = input('Desea ingresar a calculadora (SI;NO)')

if (calculadora == 'SI'):       
    while (calculadora == 'SI'):
        # Ingresa operacion
        operacion = input('Operacion (Suma(+);Resta(-);Multiplicacion(*);Division(/);Exponenciacion(**); FIN(Salir)')

        # Verifica, finaliza (break)
        if (operacion == 'FIN'):
            break

        # Ingresa operadores
        operador1 = int(input('Ingrese el primer operador  \n'))
        operador2 = int(input('Ingrese el segundo operador \n'))


        # verifica operacion y calcula
        if (operacion == '+'):
            opera = 'Sumar'
            resultado = operador1 + operador2 
        elif (operacion == '-'):
            opera = 'Restar '
            resultado = operador1 - operador2
        elif (operacion == '*'):
            opera = 'Multiplicar'
            resultado = operador1 * operador2    
        elif (operacion == '/'):
            opera = 'Divisir'
            resultado = 0
            if (operador2 >  0):
                resultado = operador1 / operador2
        elif (operacion == '**'):
            opera = 'Exponenciar'
            resultado = operador1 ** operador2
        else:
            opera = 'S/O'

        # Verifica, si la operacion ingresada es correcta
        if (opera == 'S/O'):   
            print('Error..OPERACION es incorrecta')
        else:
            # Imprime resultado operacion
            print('Resultado de ', opera, ' operador1 ', operador1, ' y ', ' operador2 es ', resultado)

        # Pregunta si desea continuar calculando    
        calculadora = input('Desea continuar usando la calculadora (SI;NO)')
    

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
