"""
/*
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */
"""
import re
def find_ohm(value1, value2):
    num1 = int(re.sub("[^0-9]","", value1))
    num2 = int(re.sub("[^0-9]","", value2))
    print(num1, num2)
    ohm = 0
    if (value1[-1] != "I" and value1[-1] != "V" and value1[-1] != "R") or (value2[-1] != "I" and value2[-1] != "V" and value2[-1] != "R") or (value1[-1] == value2[-1]):
        print("Invalid value")
        return
    
    if (value1[-1] == "V" and value2[-1] == "I") or (value1[-1] == "I" and value2[-1] == "V"):
        ohm = num1 / num2 if (value1[-1] == "V" and value2[-1] == "I") else num2 / num1
        print("R = {:.2f}".format(ohm))
        return
    
    if (value1[-1] == "V" and value2[-1] == "R") or (value1[-1] == "R" and value2[-1] == "V"):
        ohm = num1 / num2 if (value1[-1] == "V" and value2[-1] == "R") else num2 / num1
        print("I = {:.2f}".format(ohm))
        return
    
    if (value1[-1] == "I" and value2[-1] == "R") or (value1[-1] == "R" and value2[-1] == "I"):
        ohm = num1 * num2 if (value1[-1] == "I" and value2[-1] == "R") else num2 * num1
        print("V = {:.2f}".format(ohm))
        return
find_ohm("5I", "12R")
