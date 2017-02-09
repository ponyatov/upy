import sys
import ply.lex  as lex
import ply.yacc as yacc
from sym import *

tokens = [ 'SYM' , 'NUM' , 'EQ','ADD','MUL' ]

t_ignore = ' \t\r'
t_ignore_comment = '\#.*'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_EQ(t):
    r'\='
    t.value = Op(t.value) ; return t
def t_ADD(t):
    r'\+'
    t.value = Op(t.value) ; return t
def t_MUL(t):
    r'\*'
    t.value = Op(t.value) ; return t

def t_NUM(t):
    r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?'
    t.value = Num(float(t.value)) ; return t
def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    t.value = Sym(t.value) ; return t
    
precedence = [
    ('right','EQ'),
    ('left','ADD'),
    ('left','MUL'),
    ]
    
def p_REPL_none(p):
    ' REPL : ' 
def p_REPL_recur(p):
    ' REPL : REPL ex '
    print p[2].dump()

def p_ex_scalar(p):
    ' ex : scalar '
    p[0] = p[1]
def p_scalar_sym(p):
    ' scalar : SYM '
    p[0] = p[1]
def p_scalar_num(p):
    ' scalar : NUM '
    p[0] = p[1]

def p_eq(p):
    ' ex : ex EQ ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_add(p):
    ' ex : ex ADD ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_mul(p):
    ' ex : ex MUL ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
    
def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lexer = lex.lex() ; lexer.input(sys.stdin.read())
# for i in iter(lexer.token,None): print i
yacc.yacc(debug=False, write_tables=False).parse()
