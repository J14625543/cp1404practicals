def main():
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()