from .libri import info_libro,libro_disponibile
def crea_utente(nome:str,cognome:str) -> dict:
    return {"nome":nome,"cognome":cognome}


def crea_biblioteca()-> dict:
    {"libri":[]}


def aggiungi_libro(biblioteca:dict,libro:dict)->None:
    biblioteca["libri"].append(libro)


def presta_libro(biblioteca:dict,libro_da_prestare:dict)->bool:
    for libro in biblioteca:
        if libro_disponibile(libro) == True:
            libro_da_prestare["copie_disponibili"]-=1
            return True
        else:
            return False
        

def restituisci_libro(biblioteca:dict,libro:dict) -> bool:
    if presta_libro(biblioteca,libro) == True:
        libro["copie_disponibili"]+=1
        return True
    else:
        return False