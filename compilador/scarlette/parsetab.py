
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'cadena coma comment flotante identificador llaved llavei numero pderecho pizquierdoprograma : funcionesfunciones : funcion funciones\n                 | emptyfuncion : identificador llavei instrucciones llavedinstrucciones : instruccion instrucciones\n                     | emptyinstruccion : identificador pizquierdo operandos pderechooperandos : elemento coma operandos\n                 | elementoelemento : numeroelemento : flotanteelemento : cadenaelemento : identificadorelemento : emptyempty : '
    
_lr_action_items = {'identificador':([0,5,6,10,12,13,22,23,],[1,1,8,8,15,-4,-7,15,]),'pizquierdo':([8,],[12,]),'numero':([12,23,],[17,17,]),'cadena':([12,23,],[18,18,]),'llaved':([6,9,10,11,14,22,],[-15,13,-15,-6,-5,-7,]),'flotante':([12,23,],[20,20,]),'coma':([12,15,17,18,19,20,21,23,],[-15,-13,-10,-12,-14,-11,23,-15,]),'llavei':([1,],[6,]),'pderecho':([12,15,16,17,18,19,20,21,23,24,],[-15,-13,22,-10,-12,-14,-11,-9,-15,-8,]),'$end':([0,2,3,4,5,7,13,],[-15,0,-1,-3,-15,-2,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'operandos':([12,23,],[16,24,]),'instruccion':([6,10,],[10,10,]),'instrucciones':([6,10,],[9,14,]),'programa':([0,],[2,]),'elemento':([12,23,],[21,21,]),'funciones':([0,5,],[3,7,]),'empty':([0,5,6,10,12,23,],[4,4,11,11,19,19,]),'funcion':([0,5,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> funciones','programa',1,'p_programa','sintaxis.py',6),
  ('funciones -> funcion funciones','funciones',2,'p_funciones','sintaxis.py',12),
  ('funciones -> empty','funciones',1,'p_funciones','sintaxis.py',13),
  ('funcion -> identificador llavei instrucciones llaved','funcion',4,'p_funcion','sintaxis.py',22),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','sintaxis.py',30),
  ('instrucciones -> empty','instrucciones',1,'p_instrucciones','sintaxis.py',31),
  ('instruccion -> identificador pizquierdo operandos pderecho','instruccion',4,'p_instruccion','sintaxis.py',40),
  ('operandos -> elemento coma operandos','operandos',3,'p_operandos','sintaxis.py',48),
  ('operandos -> elemento','operandos',1,'p_operandos','sintaxis.py',49),
  ('elemento -> numero','elemento',1,'p_elemento_numerico','sintaxis.py',58),
  ('elemento -> flotante','elemento',1,'p_elemento_flotante','sintaxis.py',66),
  ('elemento -> cadena','elemento',1,'p_elemento_cadena','sintaxis.py',74),
  ('elemento -> identificador','elemento',1,'p_elemento_identificador','sintaxis.py',82),
  ('elemento -> empty','elemento',1,'p_elemento_vacio','sintaxis.py',90),
  ('empty -> <empty>','empty',0,'p_empty','sintaxis.py',94),
]
