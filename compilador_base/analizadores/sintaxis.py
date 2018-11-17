import sys

arbol_sintactico = []

def p_programa(p):
    """programa : instrucciones"""
    global arbol_sintactico

    arbol_sintactico += p[1]

def p_instrucciones(p):
    """instrucciones : instruccion instrucciones
                     | empty"""

    p[0] = []

    if len(p) == 3:
        p[0] += [p[1]] + p[2]


def p_instruccion(p):
    """instruccion : identificador operandos punto_y_coma"""

    p[0] = {
        "id": p[1],
        "operandos": p[2]
    }

def p_operandos(p):
    """operandos : elemento coma operandos
                 | elemento"""

    if len(p) == 4:
        p[0] = [p[1]] + p[3]

    else:
        p[0] = [p[1]]

def p_elemento_numerico(p):
   """elemento : numero"""

   p[0] = {
        "tipo":"numero"
      , "valor":int(p[1])
   }

def p_elemento_identificador(p):
   """elemento : identificador"""

   p[0] = {
        "tipo":"identificador"
      , "valor":p[1]
   }

def p_elemento_vacio(p):
   """elemento : empty"""
   pass

def p_empty(p):
   """empty : """
   pass

def p_error(pila):
   print "Error de sintaxis: t_%s '%s' inesperado en linea %s" % (pila.type, pila.value, pila.lexer.lineno)
   sys.exit()
