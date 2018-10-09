# coding=utf-8
from os import system, name, path
from _dict import *

def mdc(dividendo, divisor):
	if divisor == 0:
		return dividendo
	else:
		return mdc(divisor, dividendo % divisor)

# Esta função usa o algoritmo de euclide extendido para encontrar o inverso multiplicativo modular de a mod m.
# O inverso de a mod m é o número x tal que ax é congruente a 1 mod m
def inverso_modular(a, m):
	# Guardamos o m inicial, pois ele pode ser usado quando o valor de x encontrado pelo algoritmo 
	# de euclides for negativo.
	m0 = m 
	y = 0
 	x = 1
	if m == 1:
   		return 0
  
	while a > 1: 
    	# q é o quociente
	    q = a // m 
	  
	  	# t é uma variável auxiliar
	    tmp = m
				  
			# m agora é o resto da divisão de a por m, segundo a regra do algoritmo de euclides
	    m = a % m 
	    a = tmp 
	    tmp = y 
	  
	    # atualizamos x and y segundo a regra da divisão inteira.
	    # a relação que vemos abaixo pode ser observada mais claramente quando executamos
	    # o algoritmo de euclides no papel. 
	    y = x - q * y 
	    x = tmp
	  
	# Caso x seja negativo, somamos ao m inicial para obter um inverso positivo.
	if x < 0: 
		x = x + m0 
  
	# Retornamos apenas x 
	return x

def define_public_key(p = 17, q = 41):
	n = int(p) * int(q)
	totiente = (p - 1) * (q - 1) # φ(n) 

	# encontrar um número "e" co-primo de totiente, maior que 1 e menor que totiente
	# ou seja, MDC(e, totiente)=1
	# chave publica (n, e)

	i = 0
	for x in xrange(3, totiente):
		if (mdc(totiente, x) == 1):
			i = i + 1
		if (i > 4): #pára depois de encontrar o quarto co-primo
			break
	e = x

	global chave_n
	global chave_e
	chave_n = n
	chave_e = e


def define_private_key(p = 17, q = 41, e = 13):
	# what now, general?
	# calcular o inverso multiplicativo modular de "e", que será a chave_d
	n = int(p) * int(q)
	totiente = (p - 1) * (q - 1)

	i = 0
	for x in xrange(3, totiente):
		if (mdc(totiente, x) == 1):
			i = i + 1
		if (i > 4): #pára depois de encontrar o quarto co-primo
			break
	e = x

	d = inverso_modular(e, totiente)

	global chave_n
	global chave_d
	chave_n = n
	chave_d = d



def generate_keys():
	global chave_n 
	global chave_e
	global chave_d

	primo1 = raw_input('Insira o primeiro número primo para gerar as chaves: (ex. 17).\n')
	primo2 = raw_input('Insira o segundo número primo para gerar as chaves: (ex. 41).\n')

	try:
		primo1 = int(primo1)
		primo2 = int(primo2)
		define_public_key(primo1, primo2)
		define_private_key(primo1,primo2,chave_e)
	except ValueError:
		print("Você precisava digitar números primos válidos, mas vamos usar 17 e 41.")
		define_public_key()
		define_private_key()

	print (boldit('\nAnote aí na ordem:\n'))
	print ('Chave pública (n, e): ('+boldit(str(chave_n)+','+str(chave_e))+')\n')
	print ('Chave privada (n, d): ('+boldit(str(chave_n)+','+str(chave_d))+')\n')
	