from biblioteca import libri


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
    autore = "Frank Herbert"
    filtrati_genere = libri.filtra_per_genere(libri_lista,genere)
    print("Libri filtrati per genere:\n")
    for libro in filtrati_genere:
        print(f"{libro['titolo']}")
    filtrati_autore = libri.filtra_per_genere(libri_lista,autore)
    print
        
if __name__ == "__main__":
    main()
