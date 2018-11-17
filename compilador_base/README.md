# Compilador Basico

Se hace uso de la libreria Python Lex-Yacc para facilitar el analisis lexico-sintactico, por lo tanto debe estar instalada:

- sudo apt-get install python-ply

# Modo de uso

python compilador.py ejemplo

# Como funciona

**fichero_de_codigo_fuente** -> **compilador.py** -> (codigo_fuente) -> **maquina_virtual.py** -> (codigo_fuente) -> **anallizadores/sintaxis.py** -> (codigo_fuente) -> **analizadores/lexico.py** -> (tokens) -> **anallizadores/sintaxis.py** -> (arbol_sintactico) -> **analizadores/semantica.py** -> (codigo intermedio) -> **maquina_virtual.py** -> ejecucion del codigo
