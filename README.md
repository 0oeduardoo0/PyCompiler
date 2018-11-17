# PyCompiler

Simulador de un compilador que lleva a cabo los siguientes procesos:

- Lectura de codigo fuente
- Analizis lexico
- Analisis sintactico
- Analisis semantico
- Generacion de codigo intermedio
- Interpretacion del codigo

La definicion del lexico/sintaxis son de un lenguaje de programacion inventado.

# Estructura del proyecto

**compilador_base**:Contiene la base de los aspectos antes mencionados del compilador, es decir, un implementación basica del compilador, con apenas unos tokens definidos, y una sintaxis bastante simple.

**compilador**: Es el compilador base pero se agrega una sintaxis mas compleja y mayor funcionalidad al lenguaje de programacion inventado.
