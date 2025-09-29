def sarous_recursivo(n):
    """
    Algoritmo recursivo de Sarous.
    Este algoritmo calcula el producto de dos números enteros usando sumas sucesivas recursivas.
    """
    if n == 0:
        return 0
    elif n > 0:
        return sarous_recursivo(n - 1) + n
    else:
        return sarous_recursivo(n + 1) + n

# Ejemplo de uso:
if __name__ == "__main__":
    numero = 5
    resultado = sarous_recursivo(numero)
    print(f"Resultado de Sarous recursivo para {numero}: {resultado}")
