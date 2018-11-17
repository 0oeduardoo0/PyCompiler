import sys
import ply.yacc as yacc
from lexico import tokens
from sintaxis import *

analizis_sintactico = yacc.yacc()

def verificar_numero_de_operandos(operandos, numero):
    if len(operandos) < numero:
        print "Error fatal: la funcion requiere %s operandos" %(numero)
        exit()

def valor_real_del_operando(variables, operando):
    if operando["tipo"] == "identificador":
        try:
            return variables[operando["valor"]]

        except:
            print "Error fatal: variable '%s' no definida" %(operando["valor"])
            exit()
    else:
        return operando

def verificar_tipo_de_operando(operando, tipo):
    if not operando["tipo"] == tipo:
        print "Error fatal: parametro (%s) inesperado" %(operando["tipo"])
        exit()

def generar_codigo_intermedio(codigo_fuente):
   codigo_fuente += "\n"
   # ver sintaxis.py
   analizis_sintactico.parse(codigo_fuente)

   # El codigo intermedio se genera como una serie de instrucciones
   # que se van a ejecutar de manera lineal
   codigo_intermedio = {}

   for pila in arbol_sintactico:
       codigo_intermedio[pila['id']] = pila['operandos']

   return codigo_intermedio
