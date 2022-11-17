"""
/*
 * Reto #45
 * CONTENEDOR DE AGUA
 * Fecha publicación enunciado: 07/10/22
 * Fecha publicación resolución: 14/11/22
 * Dificultad: MEDIA
 *
 * Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
 * de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹ 
 *          ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
 *   Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
 *
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */
"""

def matrix_blocks(blocks_num):
	matrix = [[]]
	for row in range(len(blocks_num)):
		for col in range(len(blocks_num)):
			if row < blocks_num[col]:
				matrix[row].append("⏹︎")
			else:
				matrix[row].append(" ")
		matrix.append([])
	matrix.pop()
	return matrix
	

def fill_water(blocks_num):
	blocks_fill = matrix_blocks(blocks_num)
	for row in range(len(blocks_fill)):
		block_open = 0
		block_close = 0
		for col in range(len(blocks_fill[row])):
			if blocks_fill[row][col] == "⏹︎" and block_open == 0:
				block_open = col + 1
			elif blocks_fill[row][col] == "⏹︎" and block_close == 0:
				block_close = col

			if 	block_open != 0 and block_close != 0:
				for i in range(block_open - 1, block_close):
					if blocks_fill[row][i] != "⏹︎":
						blocks_fill[row][i] = "💧"

					col -= 1
					
				block_open = 0
				block_close = 0

	blocks_fill.reverse()
	return blocks_fill

def print_fill_water(blocks_num):
	blocks_water_fill = fill_water(blocks_num)
	[print(x) for x in blocks_water_fill]

print_fill_water([4, 1, 3, 6, 1, 5])