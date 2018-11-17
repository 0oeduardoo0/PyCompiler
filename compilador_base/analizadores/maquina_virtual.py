import sys
import semantica

# este arreglo servira como espacio de memoria
# para las variables que el lenguaje "compilado" maneje
variables = {}

# A continuacion se definen las
# funciones "pre-compiladas" o "del nucleo" de nuestro lenguaje
# "compilado"

"""
f_sumar

En la sintaxis de nuestro lenguaje se define como:

sumar(n1, n1, resultado)

n1: numero a sumar
n2: numero a sumar con el primero
resultado: variable en la que se almacena el resultado
"""
def f_sumar(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 3)

    # Si las operandos son variables hay que obtener su valor real
    a = semantica.valor_real_del_operando(variables, operandos[0])
    b = semantica.valor_real_del_operando(variables, operandos[1])

    # Se verifica que el tipo de operandos sea al correcto
    semantica.verificar_tipo_de_operando(a, 'numero')
    semantica.verificar_tipo_de_operando(b, 'numero')
    semantica.verificar_tipo_de_operando(operandos[2], 'identificador')

    r = a["valor"] + b["valor"]

    variables[operandos[2]["valor"]] = {
        "tipo": "numero",
        "valor": r
    }

"""
f_mostrar

En la sintaxis de nuestro lenguaje se define como:

mostrar(foo, var [, baz])

Imprime en consola el valor de los N parametros recibidos
"""
def f_mostrar(operandos):
    global variables

    a = ""

    for operando in operandos:
        b = semantica.valor_real_del_operando(variables, operando)["valor"]
        a += str(b)

    print a

"""
f_variable

En la sintaxis de nuestro lenguaje se define como:

variable(foo)

Crea una variable de tipo indefinido lista para almacenar un valor
"""
def f_variable(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 1)
    semantica.verificar_tipo_de_operando(operandos[0], 'identificador')

    variables[operandos[0]["valor"]] = None

instrucciones_pre_compiladas = {
    "sumar": f_sumar,
    "mostrar": f_mostrar,
    "variable": f_variable
}

codigo_intermedio = {}

def ejecutar_instruccion(instruccion, operandos):
    global codigo_intermedio
    global instrucciones_pre_compiladas

    try:

        funcion = instrucciones_pre_compiladas[instruccion]
        funcion(operandos)

    except:
        print "Error fatal: %s()" %(instruccion["id"])
        exit()


def ejecutar(codigo_fuente):
    global codigo_intermedio

    # ver semantica.py generar_codigo_intermedio()
    codigo_intermedio = semantica.generar_codigo_intermedio(codigo_fuente)

    for instruccion, operandos in codigo_intermedio.iteritems():
        ejecutar_instruccion(instruccion, operandos)
