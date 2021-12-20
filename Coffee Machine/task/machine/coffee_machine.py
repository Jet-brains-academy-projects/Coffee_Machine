class CoffeeMachine:
    import sys

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def actions(self):
        action = input('Write action (buy, fill, take, remaining, exit):')
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.remaining()
        elif action == 'exit':
            self.sys.exit()

    def buy(self):
        print()
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
        coffee_type = input()
        if coffee_type == '1':
            self.espresso()
        elif coffee_type == '2':
            self.latte()
        elif coffee_type == '3':
            self.cappuccino()
        elif coffee_type == 'back':
            self.actions()

    def fill(self):
        print('Write how many ml of water you want to add:')
        add_water = int(input())
        print('Write how many ml of milk you want to add:')
        add_milk = int(input())
        print('Write how many grams of coffee beans you want')
        add_coffee_beans = int(input())
        print('Write how many disposable coffee cups you want to add:')
        add_cups = int(input())
        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_coffee_beans
        self.cups += add_cups

    def take(self):
        global money
        print(f'I gave you {self.money}')
        self.money = 0

    def espresso(self):
        if self.water - 250 > 0 and self.coffee_beans - 16 > 0 and self.cups - 1 > 0:
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            self.money += 4
        else:
            print('Sorry, not enough resources!')
            print()
            self.actions()

    def latte(self):
        if self.water - 350 > 0 and self.coffee_beans - 20 > 0 and self.cups - 1 > 0 and self.milk - 75 > 0:
            self.water -= 350
            self.coffee_beans -= 20
            self.milk -= 75
            self.cups -= 1
            self.money += 7
        else:
            print('Sorry, not enough resources!')
            print()
            self.actions()

    def cappuccino(self):
        if self.water - 200 > 0 and self.coffee_beans - 12 > 0 and self.cups - 1 > 0 and self.milk - 100 > 0:
            self.water -= 200
            self.coffee_beans -= 12
            self.milk -= 100
            self.cups -= 1
            self.money += 6
        else:
            print('Sorry, not enough resources!')
            print()
            self.actions()

    def main(self):
        while True:
            if self.actions():
                continue
            elif self.actions() == 'exit':
                break


cm = CoffeeMachine()
cm.main()
