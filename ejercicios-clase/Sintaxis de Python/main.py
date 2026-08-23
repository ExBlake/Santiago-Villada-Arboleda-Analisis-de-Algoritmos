# print("Hola, mundo")

# n = 10000
# print(type(n))
tiempo = 0.0034
# print(type(tiempo))
# algoritmo = "algoritmo de ordenamiento"
# print(type(algoritmo))
# ordenado = True
# print(type(ordenado))
# resultado = None
# print(type(resultado))

# if tiempo < 0.001:
#     categoria = "rapido"
# elif tiempo < 0.01:
#     categoria = "moderado o normal"
# else:
#     categoria = "lento"
    
# print(categoria)

# Estructuras ciclicas o repetitivas
# for i in range(2, 15, 2):
#     print(i)

# while
# intentos = 0
# while intentos < 3:
    # intentos = intentos + 1
    # print (intentos)

# Funciones

# def contar_comparaciones(lista):
#     comparaciones = 0
#     for i in range(1, len(lista)):
#         j = i
#         while j > 0 and i < 0:
#             print("Mensaje")
#     return j

# Estructura de datos nativas de Python
# Lista

# numeros = [5,2,9,1]
# print(numeros[-1])

# # Tuplas
# puntos = (1000, 0.34, True, 3.14)
# print(puntos[-1])

# # Diccionario
# tiempo = {
#     1000: 0.0002,
#     10000: 0.0034,
#     100000: 0.1,
#     "llave1": 100
# }
# print(tiempo.get("llave1"))

# # Conjuntos
# tamanios = {100,1000,100000,20000}

# Situación: quieres construir la lista de los cuadrados de los tamaños de entrada que vas a probar: [100, 1000, 10000] → [10000, 1000000, 100000000].

#For clasico
# tamanios = [100, 1000, 10000]
# cuadrados = []
# for t in tamanios:
#     cuadrados.append(t ** 2)   
    
# Compresion de lista
# cuadrados = [i ** 2 for i in tamanios]
    
# print(cuadrados)

# print(1000/0)

# try:
#     print(1000/2)
#     a = 2 
#     a.sort()
# except ZeroDivisionError:
#     print("No se puede dividir entre cero")
# except AttributeError:
#     print("EL metodo sort solo se puede aplicar a listas")
# except Exception as e:
#     print("Ocurrio un error: ", e)
# print("El programa se sigue ejecutando")
