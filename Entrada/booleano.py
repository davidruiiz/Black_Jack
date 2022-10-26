"""
Módulo que agrupa todas las funcionalidades
que permiten pedir una entrada cuya respuesta es SI o NO
"""

SI = ("s", "si", "y", "yes", "1")



def pedir_entrada_si_o_no(invite):
    """Por defecto, toda respuesta no comprendida será NO"""
    try:
        return input(invite).lower() in SI
    except:
        return False