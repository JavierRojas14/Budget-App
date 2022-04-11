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
    bar_chart = None
    datos_para_hacer_grafico = obtener_porcentajes_de_gasto(categories)
    lineas_del_grafico = {}

    for i in range(100, -10, -10):
        lineas_del_grafico[i] = f'{i:4}|'
    
    # Se me ocurre que cada linea se le edite las lineas desde su porcentaje hacia abajo.
    # Ej: Si una categoria tiene el 70% de los gastos, entonces las lineas de lineas_del_mensaje
    # desde el lineas_del_mensaje[70] hasta el lineas_del_mensaje[0] se le deben agregar o en la 
    # columna 1!.
    for categoria in datos_para_hacer_grafico.keys():
        if categoria != 'Total':
            porcentaje_de_categoria = datos_para_hacer_grafico[categoria]
            agregar_os = False

            for numero_linea in lineas_del_grafico.keys():
                if numero_linea == porcentaje_de_categoria:
                    agregar_os = True

                if agregar_os:
                    lineas_del_grafico[numero_linea] += f' o'
    
    bar_chart = 'Percentage spent by category \n'
    for numero_linea in lineas_del_grafico.keys():
        bar_chart += f'{lineas_del_grafico[numero_linea]} \n'    

    largo_barra_final = len(lineas_del_grafico[0])
    barra_horizontal = ''

    for i in range(largo_barra_final + 2):
        if i < 5:
            barra_horizontal += ' '
        
        else:
            barra_horizontal += '-'

    bar_chart += barra_horizontal

    return str(bar_chart)

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
