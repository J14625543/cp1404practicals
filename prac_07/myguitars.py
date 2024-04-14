class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.cost}"

    def __lt__(self, other):
        return self.year < other.year


def read_guitars_from_file():
    guitars = []
    with open("guitar.csv", 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def write_guitars_to_file(guitars):
    with open("guitar.csv", 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_new_guitar(guitars):
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    guitars.append(Guitar(name, year, cost))


def main():
    guitars = read_guitars_from_file()

    print("Guitars before sorting:")
    display_guitars(guitars)

    guitars.sort()

    print("\nGuitars after sorting by year:")
    display_guitars(guitars)

    add_new_guitar(guitars)

    print("\nUpdated list of guitars:")
    display_guitars(guitars)

    write_guitars_to_file(guitars)
    print("\nGuitars written to file.")


if __name__ == "__main__":
    main()