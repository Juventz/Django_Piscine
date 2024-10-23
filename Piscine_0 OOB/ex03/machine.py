import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.drinks_served = 0
        self.is_broken = False

    def repair(self):
        print("Repairing the coffee machine...")
        self.drinks_served = 0
        self.is_broken = False
        print("Machine repaired and ready to serve!")

    def serve(self, beverage_class):
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()

        if random.choice([True, False]):
            drink = beverage_class()
        else:
            drink = CoffeeMachine.EmptyCup()

        self.drinks_served += 1

        if self.drinks_served >= 10:
            self.is_broken = True

        return drink


def main():
    print()
    machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]

    try:

        print("Attempting to serve...\n")
        for _ in range(10):
            beverage = machine.serve(random.choice(beverages))
            print(beverage)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    print("-" * 20)
    print()

    try:
        print("Attempting to serve while machine is broken...")
        machine.serve(Coffee)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    print("-" * 20)

    print("\nRepairing the machine...")
    machine.repair()
    print("-" * 20)
    print()

    try:
        print("Attempting to serve after repair...\n")
        for _ in range(10):
            beverage = machine.serve(random.choice(beverages))
            print(beverage)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()
