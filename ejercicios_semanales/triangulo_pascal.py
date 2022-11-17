"""
/*
 * Reto #40
 * TRIÁNGULO DE PASCAL
 * Fecha publicación enunciado: 03/10/22
 * Fecha publicación resolución: 10/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */
"""

def draw_triangle_pascal(floors):
	pascal_floors = [[1], [1,1]]
	for i in range(2, floors):
		pascal_floors.append([1]) 
		for x in range(1, (i)):
			pascal_floors[i].append(pascal_floors[i-1][x - 1] + pascal_floors[i-1][x])
		pascal_floors[i].append(1)
	
	length = len(pascal_floors)
	print(length)
	for i in range(len(pascal_floors)):
		print("{}{}".format(" "* (length), "".join(str(pascal_floors[i][x]) + " " for x in range(len(pascal_floors[i])))))
		length -= 1
		
# 1
#121
draw_triangle_pascal(10)
