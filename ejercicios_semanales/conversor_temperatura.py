"""
/*
 * Reto #42
 * CONVERSOR DE TEMPERATURA
 * Fecha publicación enunciado: 17/10/22
 * Fecha publicación resolución: 24/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 * - ¿Quieres emplear lo aprendido en este reto?
 *   Revisa el reto mensual y crea una App: https://retosdeprogramacion.com/mensuales2022
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */
"""

def convert_temp(temp):
	converted = 0
	if temp[-1] != "C" and temp[-1] != "F" or temp[-2] != "°":
		print('La temperatura que ingreso no corresponde a grados celsius o farenheit \no no ingreso el simbolo de grados °')
		return

	if temp[-1] == "F":
		converted = int(temp.replace("°F", ""))
		converted = (converted - 32) / 1.8

		print("{:.2f}{}".format(converted, "°C"))
		return
	
	converted = int(temp.replace("°C", ""))
	converted = (converted * 1.8) + 32
	print("{:.2f}{}".format(converted, "°F"))
	

convert_temp("100°F")