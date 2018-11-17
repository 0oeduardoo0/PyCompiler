import ply.lex as lex

tokens = (
    "identificador",
    "numero",
    "flotante",
    "cadena",
    "coma",
    "pderecho",
    "pizquierdo",
    "llavei",
    "llaved",
    'comment',
)

t_identificador = r'(\w+)'
t_numero = r'([0-9]+)'
t_flotante   = r'([0-9]+)(\.)([0-9]+)'
t_cadena  = r'(\".*?\")'
t_coma = r'\,'
t_pderecho = r'\)'
t_pizquierdo = r'\('
t_llavei = r'\{'
t_llaved = r'\}'
t_ignore = ' \t'

def t_ignore_salto(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
   print "Simbolo ilegal '%s'" % (t.value[0])
   exit()

def t_ignore_comment(t):
   r'\#.*'
   pass

analizador_lexico = lex.lex()

def parse_tokens(input):
   lexer.input(input)

   while 1:

      token = lexer.token()

      if not token:
         break

      print token
