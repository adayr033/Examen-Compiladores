import ply.lex as lex

resultado_lexema = []

# Palabras reservadas
reserved = {
    'USING': 'USING',
    'NAMESPACE': 'NAMESPACE',
    'MAIN': 'MAIN',
    'CLASS': 'CLASS',
    'INT': 'INT',
    'STATIC': 'STATIC',
    'VOID': 'VOID',
    'STRING': 'STRING',
    'ARGS': 'ARGS',
    'SYSTEM': 'SYSTEM',
    'CONSOLE': 'CONSOLE',
    'WRITELINE': 'WRITELINE',

   # 'HTML':'HTML',
   # 'HEAD': 'HEAD',
   # 'TITLE': 'TITLE',
   # 'BODY': 'BODY',
   # 'H': 'H',
}

tokens = [
    'IDENTIFICADOR',
    #'IDENTIFICADOR',
    # Simbolos
    #'DIV',
    #'INTERROGACION',
    #'MAYORQUE',
    #'MENORQUE',
    #'ENTERO',
    #'PUNTOCOMA',
    #'COMSIMP',
    #'COMDOB',
    #'COMMENT',
    'CADENA',
    'SUMA',
    'RESTA',
    'MULT',
    'POTENCIA',
    'MODULO',
    'PLUSPLUS',
    'MINUSMINUS',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    'PUNTO',
    'PUNTOCOMA', 
]+ list(reserved.values())

#t_DIV = r'/'
#t_INTERROGACION = r'\?'
#t_PUNTOCOMA = r';'

t_CADENA = r'\"([^\\\n]|(\\.))*?\"'

t_MULT = r'\*'
t_MODULO = r'\%'

t_MINUSMINUS = r'\-\-'

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

t_PUNTO = r'\.'
t_PUNTOCOMA = r';'



# Regla para identificadores
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z]*'
    if t.value.upper() in reserved: 
        t.type = reserved[t.value.upper()]  
    else:
        t.type = 'IDENTIFICADOR'  
    return t

# Regla para números
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para comentarios
def t_COMMENT(t):
    r'//.*'
    pass

# Ignorar caracteres como espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter inválido '%s' en la posición %d" % (t.value[0], t.lexpos))
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Construir el analizador léxico
lexer = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)