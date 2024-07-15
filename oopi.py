class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.shift = shift
        self.pay_rate = pay_rate

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift

    def get_pay_rate(self):
        return self.pay_rate

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate
def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift = int(input("Enter Shift Number (1 for day, 2 for night): "))

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", name)
    print("Employee Number:", number)
    if shift == 1:
        print("Shift: Day")
    elif shift == 2:
        print("Shift: Night")
    print("Pay Rate:", pay_rate)

    employee = ProductionWorker(name, number, shift, pay_rate)
    print("\nEmployee object created successfully!")

if __name__ == "__main__":
    main()
