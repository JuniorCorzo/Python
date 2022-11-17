"""
* Reto #43
 * TRUCO O TRATO
 * Fecha publicación enunciado: 24/10/22
 * Fecha publicación resolución: 02/11/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y
 * un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
"""
import random as rd

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

def trick(persons):
	scare = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
	result = [""] * len(persons)
	nums_par = 0
	all_height = 0

	for i in range(len(persons)):
		if persons[i].age % 2 == 0:
			nums_par += 2
		
		all_height += persons[i].height 
		
	for i in range(len(persons)): 
		#cada 2 letras del nombre es un susto
		for j in range(int(len(persons[i].name) / 2)):
			result[i] += " " + scare[rd.randint(0, len(scare) - 1)]
		
		#por cada persona que su edad sea par agrega 2 sustos
		for j in range(nums_par):
			result[i] += " " + scare[rd.randint(0, len(scare) - 1)]

		#por cada 100 cm de altura entre todas las personas añade tres sustos
		for j in range(int(all_height / 100)):
			result[i] += " " + scare[rd.randint(0, len(scare) - 1)]
		
		print(persons[i].name, " ", result[i])	

def treat(persons):
	candys = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
	result = [" "] * len(persons)
	for i in range(len(persons)):
		#Por cada letra del nombre da un caramelo
		for j in range(len(persons[i].name)):
			result[i] += " " + candys[rd.randint(0, len(candys) - 1)]
		
		#por cada 3 años cumplidos da un dulce hasta un maximo de 10 años
		for j in range(3 if persons[i].age >= 9 else int( persons[i].age / 3)):
			result[i] += " " + candys[rd.randint(0, len(candys) - 1)]
		
		#por cada 50 cm de altura da dos dulces hasta un maximo de 150 cm
		for j in range(6 if persons[i].height >= 150 else int( persons[i].height / 50) * 2):
			result[i] += " " + candys[rd.randint(0, len(candys) - 1)]

		print(persons[i].name, " ", result[i])

persons = [Person("Angelica", 12, 133), Person("David", 20, 155), Person("Raul", 43, 177), Person("Jesus", 20, 180)]
treat(persons)