import ply.lex as lex

expresiones = ['apagate','avanza','gira_izquierda','coge_zumbador','deja_zumbador','sal_de_instruccion']
sentencias = ['si','entonces','sino','mientras','hacer','repetir','veces','y','o','si_es_cero','precede','sucede']
booleanos = ['frente_libre','junto_a_zumbador','orientado_al_norte','frente_bloqueado','no_junto_a_zumbador','orientado_al_sur','izquierda_libre','algun_zumbador_en_la_mochila',
           'orientado_al_este','izquierda_bloqueada','ningun_zumbador_en_la_mochila','orientado_al_oeste','derecha_libre','no_orientado_al_norte','derecha_bloqueada',
           'no_orientado_al_sur','no_orientado_al_este','no_orientado_al_oeste']
declaraciones = ['iniciar_programa','inicia_ejecucion','termina_ejecucion','finalizar_programa','define_nueva_instruccion','como','define_prototipo_instruccion']

tokens = ['NEWLINE',"PuntoYComa"]+ expresiones + sentencias + booleanos + declaraciones 


t_ignore = ' \t'
t_NEWLINE = r' \n'
t_PuntoYComa = r' ;'
#Expresiones
t_apagate = r'apagate'
t_avanza = r'avanza'
t_gira_izquierda = r'gira-izquierda'
t_coge_zumbador = r'coge-zumbador'
t_deja_zumbador = r'deja-zumbador'
t_sal_de_instruccion = r'sal-de-instruccion'
#Sentencias
t_si = r'si'
t_entonces = r'entonces'
t_sino = r'sino'
t_mientras = r'mientras'
t_hacer = r'hacer'
t_repetir = r'repetir'
t_veces = r'veces'
t_y = r'y'
t_o = r'o'
t_si_es_cero = r'si-es-cero'
t_precede = r'precede'
t_sucede = r'sucede'
#Booleanos
t_frente_libre = r'frente-libre'
t_junto_a_zumbador = r'junto-a-zumbador'
t_orientado_al_norte = r'orientado-al-norte'
t_frente_bloqueado = r'frente-bloqueado'
t_no_junto_a_zumbador = r'no-junto-a-zumbador'
t_orientado_al_sur = r'orientado-al-sur'
t_izquierda_libre = r'izquierda-libre'
t_algun_zumbador_en_la_mochila = r'algun-zumbador-en-la-mochila'
t_orientado_al_este = r'orientado-al-este'
t_izquierda_bloqueada = r'izquierda-bloqueada'
t_ningun_zumbador_en_la_mochila = r'ningun-zumbador-en-la-mochila'
t_orientado_al_oeste = r'orientado-al-oeste'
t_derecha_libre = r'derecha-libre'
t_no_orientado_al_norte = r'no-orientado-al-norte'
t_derecha_bloqueada = r'derecha-bloqueada'
t_no_orientado_al_sur = r'no-orientado-al-sur'
t_no_orientado_al_este = r'no-orientado-al-este'
t_no_orientado_al_oeste = r'no-orientado-al-oeste'
#Declaraciones
t_iniciar_programa = r'iniciar-programa'
t_inicia_ejecucion = r'inicia-ejecucion'
t_termina_ejecucion = r'termina-ejecucion'
t_finalizar_programa = r'finalizar-programa'
t_define_nueva_instruccion = r'define-nueva-instruccion'
t_como = r'como'
t_define_prototipo_instruccion = r'define-prototipo-instruccion'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

expresiones = open("expresionesKarel.in", "r")
listaExpresiones = expresiones.readlines()

lex.lex() # Build the lexer
for x in listaExpresiones:
    lex.input(x)

    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
