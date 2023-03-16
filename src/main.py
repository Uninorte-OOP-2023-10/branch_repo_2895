# Main File
from company.company import Company
from user.person import Person

def main() -> None:
    name = input('Digite su nombre: ')
    age = int(input('Digite su edad: '))
    company1 = Person(name, age)
    nit = input('Digite el nit: ')
    name = input('Digite el nombre de la compañia: ')
    company1 = Company(nit, name)


if __name__ == '__main__':
    main()