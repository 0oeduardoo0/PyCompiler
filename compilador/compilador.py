import sys
from scarlette import maquina_virtual

try:

    archivo = sys.argv[1]

except:

    print "Error"
    print "Indique archivo para interpretar"

    sys.exit()

programa_fuente = open(archivo)
codigo_fuente   = programa_fuente.read()

programa_fuente.close()

maquina_virtual.ejecutar(codigo_fuente)
