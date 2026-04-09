from biblioteca import libri,prestiti


def main():
    l1 = libri.crea_libro("1984", "George Orwell", "Fantascienza", 1)
    l2 = libri.crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
    l3 = libri.crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1)
    l4 = libri.crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3)
    stringa1 = libri.info_libro(l1)
    stringa2 = libri.info_libro(l2)
    stringa3 = libri.info_libro(l3)
    stringa4 = libri.info_libro(l4)
    print(f"{stringa1}\n{stringa2}\n{stringa3}\n{stringa4}")
    libri_lista = [l1,l2,l3,l4]
    genere = "Fantascienza"
    autore = "Il piccolo principe"
    filtrati_genere = libri.filtra_per_genere(libri_lista,genere)
    print("Libri filtrati per genere:")
    for libro_genere in filtrati_genere:
        print(f"{libro_genere['titolo']}")
    filtrati_autore = libri.filtra_per_genere(libri_lista,autore)
    print("Libri filtrati per autore:")
    for libro_autore in filtrati_autore:
        print(f"{libro_autore['titolo']}")
    disponibili = libri.libri_disponibili(libri_lista)
    print("Libri disponibili:")
    for libro_disp in disponibili:
        print(f"{libro_disp['titolo']}")
    


    u1 = prestiti.crea_utente("Mario", "Rossi")
    u2 = prestiti.crea_utente("Laura", "Bianchi")
    u3 = prestiti.crea_utente("Carlo", "Verdi")
    biblioteca = prestiti.crea_biblioteca()
    prestiti.aggiungi_libro(biblioteca,)



        
if __name__ == "__main__":
    main()
