# Main File
from company.company import Company

def main() -> None:
    nit = input('Digite el nit: ')
    name = input('Digite el nombre de la compañia: ')
    company1 = Company(nit, name)


if __name__ == '__main__':
    main()