def crea_libro(titolo: str, autore: str, genere: str, copie_disponibili: int) -> dict:
    return {"titolo":titolo,"autore":autore,"genere":genere,"copie_disponibili":copie_disponibili}


def info_libro(libro: dict) -> str:
    stringa = f"{libro['titolo']} di {libro['autore']}({libro['genere']}) -Copie disponibili: {libro["copie_disponibili"]}"
    return stringa


def libro_disponibile(libro: dict) -> bool:
    if libro["copie_disponibili"] > 0:
        return True
    else:
        return False