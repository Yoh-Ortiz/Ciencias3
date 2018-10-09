import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','NEWLINE' ]


t_ignore = ' \t'
t_NEWLINE = r' \n'
t_PLUS = r'SUM'
t_MINUS = r'RES'
t_TIMES = r'MUL'
t_DIVIDE = r'DIV'
t_EQUALS = r'IGU'
t_NAME = r'[a-z][a-z]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

expresiones = open("expresionesNEW.in", "r")
listaExpresiones = expresiones.readlines()

lex.lex() # Build the lexer
for x in listaExpresiones:
    lex.input(x)

    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
