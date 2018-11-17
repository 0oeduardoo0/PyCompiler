import sys
from analizadores import maquina_virtual

try:

    archivo = sys.argv[1]

except:

    print "Error"
    print "Indique archivo para interpretar"

    sys.exit()

# se abre el archivo del codigo fuente
programa_fuente = open(archivo)
# se obtiene el codigo fuente
codigo_fuente   = programa_fuente.read()

programa_fuente.close()

# ver analizadores/maquina_virtual.py ejecutar()
maquina_virtual.ejecutar(codigo_fuente)
