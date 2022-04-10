class Category:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        objeto = {'amount': amount, 'description': description}
        self.ledger.append(objeto)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            objeto = {'amount': - amount, 'description': description}
            self.ledger.append(objeto)
            return True
        
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        
        return balance

    def transfer(self, amount, categoria): 
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {categoria.nombre}')
            categoria.deposit(amount, f'Transfer from {self.nombre}')

            return True
        
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance:
            return False
        
        else:
            return True

    def __str__(self):
        # Imprimir una linea de 30 carácteres, donde el nombre de la categoría 
        # está centrada en una linea de *

        # Luego, una lista de cada 
        return
    

# Esta función recibirá hasta 4 categorías. 
def create_spend_chart(categories):
    return str(bar_chart)