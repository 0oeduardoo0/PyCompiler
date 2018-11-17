import ply.lex as lex

tokens = (
    "identificador",
    "numero",
    "coma",
    "pderecho",
    "pizquierdo",
    "punto_y_coma"
)

t_identificador = r'(\w+)'
t_numero = r'([0-9]+)'
t_coma = r'\,'
t_pderecho = r'\)'
t_pizquierdo = r'\('
t_punto_y_coma = r'\;'
t_ignore = ' \t'

def t_ignore_salto(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
   print "Error: simbolo ilegal '%s' en linea %s" % (t.value[0], t.lexer.lineno)
   exit()

analizador_lexico = lex.lex()

def parse_tokens(input):
   lexer.input(input)

   while 1:

      token = lexer.token()

      if not token:
         break

      print token
