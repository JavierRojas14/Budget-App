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
        if amount > self.get_balance():
            return False
        
        else:
            return True

    def __str__(self):
        mensaje = f'{self.nombre.center(30, "*")}\n'

        for i in self.ledger:
            if len(i['description']) > 23:
                description = i['description'][:23]

            else:
                description = f'{i["description"]:23}'
            
            amount = f'{i["amount"]:>7.2f}'

            linea = f'{description}{amount}\n'

            mensaje += linea
            
        final = f'Total: {self.get_balance()}'
        mensaje += final

        return mensaje
    

# Esta función recibirá hasta 4 categorías. 
def create_spend_chart(categories):
    datos_para_hacer_grafico = obtener_porcentajes_de_gasto(categories)
    return datos_para_hacer_grafico

def obtener_porcentajes_de_gasto(categories):
    todo_lo_gastado = {}

    total_gastado = 0
    for categoria in categories:
        gastado_por_categoria = 0
        for transaccion in categoria.ledger:
            if transaccion['amount'] < 0:
                gastado_por_categoria += transaccion['amount']
            
        todo_lo_gastado[f'{categoria.nombre}'] = gastado_por_categoria
        total_gastado += gastado_por_categoria
    
    todo_lo_gastado['Total'] = total_gastado

    for nombre_categoria in todo_lo_gastado.keys():
        porcentaje = (todo_lo_gastado[nombre_categoria] / todo_lo_gastado['Total']) * 100
        porcentaje = round(porcentaje / 10) * 10
        todo_lo_gastado[nombre_categoria] = porcentaje

    return todo_lo_gastado 
            



    return str(bar_chart)