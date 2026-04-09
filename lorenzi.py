from biblioteca import libri,prestiti


def main():
    l1 = libri.crea_libro("1984", "George Orwell", "Fantascienza", 1)
    l2 = libri.crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
    l3 = libri.crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1)
    l4 = libri.crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3)
    stringa1 = libri.info_libro(l1)
    stringa2 = libri.info_libro(l2)
    stringa3 = libri
