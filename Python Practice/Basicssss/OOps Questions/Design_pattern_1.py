## Factory Design Pattern
## Modular programming in Python

## Coffee Shop --> Espresso, Latte, Cappuccino

from abc import abstractmethod, ABC

class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."
    
class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte."
    
class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino."
    
##Implement the Factory(CoffeeMachine)
class CoffeeMachine:
    def make_cofee(self, coffee_type):
        if coffee_type == 'Espresso':
            return Espresso().prepare()
        
        elif coffee_type == 'Latte':
            return Latte().prepare()
        
        elif coffee_type == 'Capuuccino':
            return Cappuccino().prepare()
        
        else:
            return "Unkonwn coffee type!"
        
if __name__ == '__main__':
    machine = CoffeeMachine()
    
    coffee = machine.make_cofee('Espresso')
    print(coffee)
    
    
    
