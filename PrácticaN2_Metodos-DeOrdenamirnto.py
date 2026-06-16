import time
import random

class OrdenadorDatos:
    """
    Clase encargada de gestionar un arreglo de números enteros
    y aplicar diferentes algoritmos de ordenamiento de forma estructurada.
    """
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los números
        self.arreglo = []

    def generar_datos_aleatorios(self, cantidad):
        """Genera una lista de números aleatorios para probar los métodos."""
        self.arreglo = [random.randint(1, 100) for _ in range(cantidad)]
        print(f"\n[+] Se han generado {cantidad} elementos aleatorios.")

    def establecer_arreglo(self, nueva_lista):
        """Permite asignar una lista específica manualmente."""
        self.arreglo = nueva_lista.copy()

    def obtener_arreglo(self):
        """Retorna el estado actual del arreglo."""
        return self.arreglo

    # =========================================================================
    # 1. MÉTODO DE ORDENAMIENTO BURBUJA (BUBBLE SORT)
    # =========================================================================
    def ordenar_burbuja(self):
        """
        Compara pares de elementos adyacentes y los intercambia si están 
        en el orden incorrecto. El proceso se repite hasta que no hay cambios.
        """
        arr = self.arreglo.copy()  # Trabajamos sobre una copia para no alterar el original
        n = len(arr)
        
        # Bucle externo que recorre todo el arreglo
        for i in range(n):
            # Bucle interno (los últimos 'i' elementos ya están en su lugar correcto)
            for j in range(0, n - i - 1):
                # Si el elemento actual es mayor que el siguiente, se intercambian
                if arr[j] > arr[j + 1]:
                    aux = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = aux
        return arr

    # =========================================================================
    # 2. MÉTODO DE ORDENAMIENTO POR INSERCIÓN (INSERTION SORT)
    # =========================================================================
    def ordenar_insercion(self):
        """
        Toma cada elemento y lo posiciona en el lugar correcto comparándolo
        con los elementos que ya se encuentran ordenados a su izquierda.
        """
        arr = self.arreglo.copy()
        
        # Recorremos desde el segundo elemento (índice 1) hasta el final
        for i in range(1, len(arr)):
            clave = arr[i]  # El elemento actual que queremos insertar
            j = i - 1
            
            # Mueve los elementos de arr[0..i-1] que son mayores que la clave
            # a una posición adelante de su posición actual
            while j >= 0 and clave < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # Colocamos la clave en su posición correcta
            arr[j + 1] = clave
        return arr

    # =========================================================================
    # 3. MÉTODO DE ORDENAMIENTO POR SELECCIÓN (SELECTION SORT)
    # =========================================================================
    def ordenar_seleccion(self):
        """
        Busca repetidamente el elemento más pequeño de la sección no ordenada
        y lo coloca al principio.
        """
        arr = self.arreglo.copy()
        n = len(arr)
        
        # Avanza el límite del subarreglo ordenado
        for i in range(n):
            indice_minimo = i
            # Busca el mínimo en el resto del arreglo sin ordenar
            for j in range(i + 1, n):
                if arr[j] < arr[indice_minimo]:
                    indice_minimo = j
            
            # Intercambia el mínimo encontrado con el primer elemento sin ordenar
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
        return arr

    # =========================================================================
    # 4. MÉTODO DE ORDENAMIENTO SHELL (SHELL SORT)
    # =========================================================================
    def ordenar_shell(self):
        """
        Es una versión mejorada de la inserción directa. Compara elementos 
        separados por un espacio (gap) que se va reduciendo a la mitad.
        """
        arr = self.arreglo.copy()
        n = len(arr)
        gap = n // 2  # Inicializamos el espacio o brecha
        
        # Reduce el gap hasta que llegue a 0
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                # Realiza un ordenamiento por inserción para este gap
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2  # Reducimos la brecha a la mitad
        return arr


# =========================================================================
# MENÚ INTERACTIVO Y EJECUCIÓN PRINCIPAL
# =========================================================================
def menu():
    ordenador = OrdenadorDatos()
    # Generamos una lista por defecto de 10 elementos
    ordenador.generar_datos_aleatorios(10)

    while True:
        print("\n" + "="*45)
        print("     SISTEMA DE MÉTODOS DE ORDENAMIENTO     ")
        print("="*45)
        print(f"Arreglo actual: {ordenador.obtener_arreglo()}")
        print("-"*45)
        print("1. Generar nuevos números aleatorios")
        print("2. Ejecutar Ordenamiento Burbuja")
        print("3. Ejecutar Ordenamiento por Inserción")
        print("4. Ejecutar Ordenamiento por Selección")
        print("5. Ejecutar Ordenamiento ShellSort")
        print("6. Salir")
        print("="*45)
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            try:
                cant = int(input("¿Cuántos números desea generar?: "))
                ordenador.generar_datos_aleatorios(cant)
            except ValueError:
                print("[-] Error: Ingrese un número entero válido.")
        
        elif opcion in ["2", "3", "4", "5"]:
            if not ordenador.obtener_arreglo():
                print("[-] El arreglo está vacío. Genere números primero.")
                continue

            # Diccionario de mapeo para ejecutar el método correspondiente y medir tiempo
            metodos = {
                "2": ("Burbuja", ordenador.ordenar_burbuja),
                "3": ("Inserción", ordenador.ordenar_insercion),
                "4": ("Selección", ordenador.ordenar_seleccion),
                "5": ("ShellSort", ordenador.ordenar_shell)
            }
            
            nombre_metodo, funcion_ordenar = metodos[opcion]
            
            # Medimos el rendimiento (tiempo de inicio)
            tiempo_inicio = time.perf_counter()
            resultado = funcion_ordenar()
            tiempo_fin = time.perf_counter()
            
            # Duración del algoritmo en milisegundos
            duracion = (tiempo_fin - tiempo_inicio) * 1000

            print(f"\n[!] Resultado usando {nombre_metodo}:")
            print(f"-> Arreglo Ordenado: {resultado}")
            print(f"-> Tiempo de ejecución: {duracion:.4f} ms")
            
        elif opcion == "6":
            print("\n[+] Saliendo del programa. ¡Éxito en tu entrega de la UDB!")
            break
        else:
            print("[-] Opción inválida. Intente de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    menu()
