import itertools

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
    primera_categoria = True
    for categoria in datos_para_hacer_grafico.keys():
        porcentaje_de_categoria = datos_para_hacer_grafico[categoria]
        
        agregar_os = False

        for numero_linea in lineas_del_grafico.keys():
            if numero_linea == porcentaje_de_categoria:
                agregar_os = True

            if agregar_os:
                if primera_categoria:
                    lineas_del_grafico[numero_linea] += f' o'
                
                else:
                    lineas_del_grafico[numero_linea] += f'  o'
        
        primera_categoria = False
    
    bar_chart = 'Percentage spent by category\n'

    for key, value in lineas_del_grafico.items():
        lineas_del_grafico[key] = value.ljust(len(lineas_del_grafico[0]), ' ')
        bar_chart += f'{lineas_del_grafico[key]}\n'   

    largo_barra_final = len(lineas_del_grafico[0])
    barra_horizontal = ''

    for i in range(largo_barra_final + 2):
        if i < 5:
            barra_horizontal += ' '
        
        else:
            barra_horizontal += '-'

    bar_chart += f'{barra_horizontal}\n'

    # Para poner los nombres en vertical, me tinca ocupar algún zip, o algo asi.
    # Onda, hacer tuplas de los nombres de las categorías [(x1, y1, z1), (x2, y2, z2) ... (xn, yn, zn)]
    leyenda = ''
    for x, y, z in itertools.zip_longest(*datos_para_hacer_grafico.keys(), fillvalue = ' '):
        nueva_linea = f'      {x}  {y}  {z} \n'
        leyenda += nueva_linea
    
    bar_chart += leyenda

    return bar_chart

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
        porcentaje = round_down(porcentaje, 10)
        todo_lo_gastado[nombre_categoria] = porcentaje

    del todo_lo_gastado['Total'] 

    return todo_lo_gastado 

def round_down(numero, divisor):
    return numero - (numero%divisor)