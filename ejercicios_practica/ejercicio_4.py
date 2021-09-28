# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Realizar un bucle "while" cuya condición de continuidad
# sea que <x sea menor a 10> y que <x sea distinto de 6>
# Colocar ambas condiciones como condicion del "while" realizando
# una condición compuesta (utilice el operador "and" o "or" según corresponda)
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

# Realice el mismo bucle "while" pero en vez de estar formado por una condición
# compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
# "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

# Bucle 1
x1 = int(input(('Ingrese numero bucle 1\n ')))
x = x1
while (x < 10) and not(x == 6):
    # incrementar x en 2
    print('Bucle 1, x vale ', x) 
    x += 2    

# Bucle 2
x2 = int(input(('Ingrese numero bucle 2\n ')))
x = x2
while (x < 10):
    if (x == 6):
        print('interrumpe bucle 2')
        break
    # incrementar x en 2    
    print('Bucle 2, x vale ', x) 
    x += 2

print("terminamos!")