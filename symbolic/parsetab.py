
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightPOWERrightUMINUSABS ACOS ASIN ATAN COMMA COS COSH DIVIDE E EXP LN LOG LPAREN MINUS NUMBER PI PLUS POWER RPAREN SEC SIN SINH SQRT TAN TANH TIMES VARIABLEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POWER expressionexpression : MINUS expression %prec UMINUSexpression : SIN LPAREN expression RPAREN\n                  | COS LPAREN expression RPAREN\n                  | LN LPAREN expression RPAREN\n                  | SQRT LPAREN expression RPAREN\n                  | ABS LPAREN expression RPAREN\n                  | EXP LPAREN expression RPAREN\n                  | SINH LPAREN expression RPAREN\n                  | COSH LPAREN expression RPAREN\n                  | TANH LPAREN expression RPAREN\n                  | ASIN LPAREN expression RPAREN\n                  | ACOS LPAREN expression RPAREN\n                  | ATAN LPAREN expression RPAREN\n                  | TAN LPAREN expression RPAREN\n                  | SEC LPAREN expression RPAREN\n                  | LOG LPAREN expression COMMA expression RPARENexpression : LPAREN expression RPARENexpression : NUMBERexpression : VARIABLEexpression : PI\n                  | E'
    
_lr_action_items = {'MINUS':([0,1,2,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[2,24,2,2,-23,-24,-25,-26,2,2,2,2,2,-6,2,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1,-2,-3,-4,-5,24,-22,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,2,24,-21,]),'SIN':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'COS':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'LN':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'SQRT':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'ABS':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'EXP':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'SINH':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'COSH':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'TANH':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'ASIN':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'ACOS':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'ATAN':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'TAN':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'SEC':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'LOG':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[4,4,29,4,31,32,33,34,35,36,37,38,39,40,41,42,43,44,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'NUMBER':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'VARIABLE':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'PI':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'E':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'$end':([1,19,20,21,22,28,45,46,47,48,49,51,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[0,-23,-24,-25,-26,-6,-1,-2,-3,-4,-5,-22,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,]),'PLUS':([1,19,20,21,22,28,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,],[23,-23,-24,-25,-26,-6,23,-1,-2,-3,-4,-5,23,-22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,23,-21,]),'TIMES':([1,19,20,21,22,28,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,],[25,-23,-24,-25,-26,-6,25,25,25,-3,-4,-5,25,-22,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,25,-21,]),'DIVIDE':([1,19,20,21,22,28,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,],[26,-23,-24,-25,-26,-6,26,26,26,-3,-4,-5,26,-22,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,26,-21,]),'POWER':([1,19,20,21,22,28,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,],[27,-23,-24,-25,-26,-6,27,27,27,27,27,27,27,-22,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,27,-21,]),'RPAREN':([19,20,21,22,28,30,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,],[-23,-24,-25,-26,-6,51,-1,-2,-3,-4,-5,66,-22,67,68,69,70,71,72,73,74,75,76,77,78,79,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,82,-21,]),'COMMA':([19,20,21,22,28,45,46,47,48,49,51,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[-23,-24,-25,-26,-6,-1,-2,-3,-4,-5,-22,80,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,23,24,25,26,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,80,],[1,28,30,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',13),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',14),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',15),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',16),
  ('expression -> expression POWER expression','expression',3,'p_expression','parser.py',17),
  ('expression -> MINUS expression','expression',2,'p_expression_unary','parser.py',30),
  ('expression -> SIN LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',35),
  ('expression -> COS LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',36),
  ('expression -> LN LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',37),
  ('expression -> SQRT LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',38),
  ('expression -> ABS LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',39),
  ('expression -> EXP LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',40),
  ('expression -> SINH LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',41),
  ('expression -> COSH LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',42),
  ('expression -> TANH LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',43),
  ('expression -> ASIN LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',44),
  ('expression -> ACOS LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',45),
  ('expression -> ATAN LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',46),
  ('expression -> TAN LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',47),
  ('expression -> SEC LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',48),
  ('expression -> LOG LPAREN expression COMMA expression RPAREN','expression',6,'p_expression_function','parser.py',49),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',84),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',88),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','parser.py',92),
  ('expression -> PI','expression',1,'p_expression_constants','parser.py',96),
  ('expression -> E','expression',1,'p_expression_constants','parser.py',97),
]
