from konsoli_io import KonsoliIO
from peli import Peli


def main():
    io = KonsoliIO()
    peli = Peli(io)

    peli.suorita()

if __name__ == "__main__":
    main()
