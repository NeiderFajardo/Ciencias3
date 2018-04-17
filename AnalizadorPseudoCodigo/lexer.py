import ply.lex as lex


tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' , 'MAYOR' , 'MAYOREQ'
, 'MINOR' , 'MINOREQ' , 'EQEQUALS' , 'DIFFERENT' , 'AND' , 'OR' , 'NOT' , 'INCREMENT' , 'DECREMENT'
, 'INCREMENTEQ' , 'DECREMENTEQ' , 'TIMESEQ' , 'DIVIDEEQ', 'LPAREN' ,'RPAREN' , 'LBRACKET'
, 'RBRACKET' , 'LBRACE' , 'RBRACE', 'QUOTES' , '2POINTS']
reserved = {
    'para' : 'PARA',
    'si' : 'SI',
    'luego' : 'LUEGO',
    'escribir' : 'ESCRIBIR',
    'leer' : 'LEER'
}
tokens += reserved.values()
t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_MAYOR = r'>'
t_MAYOREQ = r'>='
t_MINOR = r'<'
t_MINOREQ = r'<='
t_EQEQUALS = r'=='
t_DIFFERENT = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_INCREMENTEQ = r'\+\='
t_DECREMENTEQ = r'\-\='
t_TIMESEQ = r'\*\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_QUOTES = r'\"'
t_2POINTS = r'\;'

def cargarArchivo(nombre):
    archivo = open(nombre, "r")
    return archivo.read()


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex() # Build the lexer

lex.input(cargarArchivo("pseudoCodigo.txt"))
while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
