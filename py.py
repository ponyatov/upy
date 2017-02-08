import sys
import ply.lex  as lex
import ply.yacc as yacc
from sym import *

tokens = [ 'SYM' , 'NUM' , 'OP' ]

t_ignore = ' \t\r'
t_ignore_comment = '\#.*'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_OP(t):
    r'[=+*]'
    t.value = Op(t.value) ; return t
def t_NUM(t):
    r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?'
    t.value = Num(float(t.value)) ; return t
def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    t.value = Sym(t.value) ; return t
    
def t_error(t): print 'lexer/error',t

lexer = lex.lex() ; lexer.input(sys.stdin.read())
for i in iter(lexer.token,None): print i