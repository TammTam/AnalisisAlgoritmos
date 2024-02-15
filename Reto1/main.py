import math


def problem_1(busqueda):
  inicio = 0
  numeros = []
  sum = 0

  while inicio < busqueda:
    if (inicio % 3 == 0) or (inicio % 5 == 0):
      numeros.append(inicio)
      sum += inicio
    inicio += 1

  return sum


def problem_2(max):
  secuencia = [1, 2]
  suma = 0
  while secuencia[-1] <= max:
    if secuencia[-1] % 2 == 0:
      suma += secuencia[-1]
    secuencia.append(secuencia[-1] + secuencia[-2])
  return suma


def problem_3(numero):
  factores = []
  for i in range(2, math.isqrt(numero) + 1):
    while numero % i == 0:
      factores.append(i)
      numero //= i
  if numero > 1:
    factores.append(numero)
  return max(factores)


def problem_4():

  def es_palindromo(numero):
    return str(numero) == str(numero)[::-1]

  def encuentra_palindromo_mas_grande():
    palindromo_maximo = 0
    for i in range(100, 1000):
      for j in range(100, 1000):
        producto = i * j
        if es_palindromo(producto) and producto > palindromo_maximo:
          palindromo_maximo = producto
    return palindromo_maximo

  return encuentra_palindromo_mas_grande()


def problem_5(limite):
  numero = limite
  divisible = False
  while not divisible:
    divisible = True
    for i in range(1, limite + 1):
      if numero % i != 0:
        divisible = False
        break
    if not divisible:
      numero += limite
  return numero
