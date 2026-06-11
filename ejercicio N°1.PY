# ─────────────────────────────────────────────────────────────────
# EJERCICIO 1: Suma y promedio de pares e impares de 1 hasta N
# ─────────────────────────────────────────────────────────────────
 
# Solicitar al usuario un número entero positivo N
N = int(input('Ingrese el valor de N: '))
 
# Inicializar acumuladores de suma para pares e impares
suma_pares   = 0   # Almacena la suma de los números pares
suma_impares = 0   # Almacena la suma de los números impares
 
# Contadores para calcular el promedio
cont_pares   = 0   # Cantidad de números pares encontrados
cont_impares = 0   # Cantidad de números impares encontrados
 
# Recorrer los números del 1 al N (inclusive) con un bucle for
for i in range(1, N + 1):
    if i % 2 == 0:         # Verificar si el número es par (resto 0)
        suma_pares   += i  # Acumular al total de pares
        cont_pares   += 1  # Incrementar contador de pares
    else:                  # Si no es par, entonces es impar
        suma_impares += i  # Acumular al total de impares
        cont_impares += 1  # Incrementar contador de impares
 
# Calcular promedios evitando división entre cero
prom_pares   = suma_pares   / cont_pares   if cont_pares   > 0 else 0
prom_impares = suma_impares / cont_impares if cont_impares > 0 else 0
