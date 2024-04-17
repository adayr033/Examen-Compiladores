import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import lexer

# Resultado del análisis
resultado_gramatica = []

def p_program(p):
    '''program : using_statement namespace_definition'''
    p[0] = p[1]

def p_using_statement(p):
    '''using_statement : USING SYSTEM PUNTOCOMA'''
    p[0] = ("Declaración using encontrada")

def p_namespace_definition(p):
    '''namespace_definition : NAMESPACE IDENTIFICADOR LLAIZQ class_definition LLADER'''
    p[0] = ("Namespace definido:", p[2], p[4])

def p_class_definition(p):
    '''class_definition : CLASS IDENTIFICADOR LLAIZQ main_method LLADER'''
    p[0] = ("Clase definida:", p[2], p[4])

def p_main_method(p):
    '''main_method : STATIC VOID MAIN PARIZQ STRING CORIZQ CORDER ARGS PARDER LLAIZQ statement LLADER'''
    p[0] = ("Función MAIN encontrada", p[12])

def p_statement(p):
    '''statement : print_statement'''
    p[0] = p[1]

def p_print_statement(p):
    'print_statement : SYSTEM PUNTO CONSOLE PUNTO WRITELINE PARIZQ CADENA PARDER PUNTOCOMA'
    p[0] = ("PRINTLN encontrado:", p[7])


# Regla para manejar errores
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintáctico de tipo {} en el valor {}".format(str(t.type), str(t.value))
    else:
        resultado = "Error sintáctico: Token inválido"
    print(resultado)
    resultado_gramatica.append(resultado)

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    
    # Realizar el análisis sintáctico en el código completo
    parser.parse(data)

    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa el dato >>> ')
        except EOFError:
            continue
        if not s:  
            continue
        
        gram = parser.parse(s)
        print("Resultado ", gram)
        prueba_sintactica(s)