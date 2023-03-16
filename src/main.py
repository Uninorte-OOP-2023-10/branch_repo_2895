# Main File
from user.person import Person

def main() -> None:
    name = input('Digite su nombre: ')
    age = int(input('Digite su edad: '))
    company1 = Person(name, age)


if __name__ == '__main__':
    main()