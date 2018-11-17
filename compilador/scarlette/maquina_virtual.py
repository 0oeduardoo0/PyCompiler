import sys
import semantica

variables = {}

def f_sumar(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 3)

    a = semantica.valor_real_del_operando(variables, operandos[0])
    b = semantica.valor_real_del_operando(variables, operandos[1])

    semantica.verificar_tipo_de_operando(a, 'numero')
    semantica.verificar_tipo_de_operando(b, 'numero')
    semantica.verificar_tipo_de_operando(operandos[2], 'identificador')

    r = a["valor"] + b["valor"]

    variables[operandos[2]["valor"]] = {
        "tipo": "numero",
        "valor": r
    }

def f_multiplicar(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 3)

    a = semantica.valor_real_del_operando(variables, operandos[0])
    b = semantica.valor_real_del_operando(variables, operandos[1])

    semantica.verificar_tipo_de_operando(a, 'numero')
    semantica.verificar_tipo_de_operando(b, 'numero')
    semantica.verificar_tipo_de_operando(operandos[2], 'identificador')

    r = a["valor"] * b["valor"]

    variables[operandos[2]["valor"]] = {
        "tipo": "numero",
        "valor": r
    }

def f_mostrar(operandos):
    global variables

    a = ""

    for operando in operandos:
        b = semantica.valor_real_del_operando(variables, operando)["valor"]
        a += str(b)

    print a

def f_variable(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 2)
    semantica.verificar_tipo_de_operando(operandos[0], 'identificador')

    a = semantica.valor_real_del_operando(variables, operandos[1])

    variables[operandos[0]["valor"]] = a

def f_comparar_igualdad(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 3)

    a = semantica.valor_real_del_operando(variables, operandos[0])
    b = semantica.valor_real_del_operando(variables, operandos[1])

    semantica.verificar_tipo_de_operando(operandos[2], 'identificador')

    if a["valor"] == b["valor"]:
        ejecutar_funcion(operandos[2]["valor"])

def f_comparar_diferencia(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 3)

    a = semantica.valor_real_del_operando(variables, operandos[0])
    b = semantica.valor_real_del_operando(variables, operandos[1])

    semantica.verificar_tipo_de_operando(operandos[2], 'identificador')

    if not a["valor"] == b["valor"]:
        ejecutar_funcion(operandos[2]["valor"])

def f_entrada_numero(operandos):
    global variables

    semantica.verificar_numero_de_operandos(operandos, 2)

    semantica.verificar_tipo_de_operando(operandos[0], "cadena")
    semantica.verificar_tipo_de_operando(operandos[1], "identificador")

    a = int(raw_input(operandos[0]["valor"]))

    variables[operandos[1]["valor"]] = {
        "tipo": "numero",
        "valor": a
    }

instrucciones_pre_compiladas = {
    "sumar": f_sumar,
    "multiplicar": f_multiplicar,
    "mostrar": f_mostrar,
    "variable": f_variable,
    "comparar_igualdad": f_comparar_igualdad,
    "comparar_diferencia": f_comparar_diferencia,
    "entrada_numero": f_entrada_numero
}

codigo_intermedio = {}

def ejecutar_instruccion(instruccion):
    global codigo_intermedio
    global instrucciones_pre_compiladas

    try:

        funcion = instrucciones_pre_compiladas[instruccion["id"]]
        funcion(instruccion["operandos"])

    except:

        try:

            funcion = codigo_intermedio[instruccion["id"]]
            ejecutar_funcion(instruccion["id"])

        except:
            print "Error fatal: %s()" %(instruccion["id"])
            exit()

def ejecutar_funcion(id):
    global codigo_intermedio

    funcion = None

    try:

        funcion = codigo_intermedio[id]

        for instruccion in funcion:
            ejecutar_instruccion(instruccion)

    except:

        print "Error fatal: %s{ ... }" %(id)
        exit()


def ejecutar(codigo_fuente):
    global codigo_intermedio

    codigo_intermedio = semantica.generar_codigo_intermedio(codigo_fuente)
    ejecutar_funcion("inicio")
