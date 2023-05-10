import time,os
# Stock inicial de productos y clientes
stock = []
clientes = {
    '1' : {'nombre' : 'Alberto', 'apellido' : 'García', 'password' : 'Alberto_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 14990},
    '2' : {'nombre' : 'Jose', 'apellido' : 'Martínez', 'password' : 'Jose_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 11990},
    '3' : {'nombre' : 'Steffania', 'apellido' : 'Schweikart', 'password' : 'Steffania_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 10990},
    '4' : {'nombre' : 'Marcos', 'apellido' : 'Alarcón', 'password' : 'Marcos_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 9990},
    '5' : {'nombre' : 'Luis', 'apellido' : 'Martínez', 'password' : 'Luis_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 8990},
    '6' : {'nombre' : 'Baltasar Fernández'}}
compras = []

# Función decorativa de cada sección
def banner(seccion):
    os.system('cls')
    print('*'*10+seccion+'*'*10)
    
# Verificar el stock antes de procesar la compra
def verifica_stock(producto,cantidad):
    if stock[producto] >= cantidad:
        return True
    else:
        return False
    
def ingresa_saldo():
    banner('Nuestros clientes')
    i = 0
    for key in listaClientes:
        print(f'{i+1}) {key.nombre} {key.apellido}')
        i += 1
    cliente = int(input('¿A qué cliente le añadiremos saldo?: '))
    ingreso = int(input('Ingrese el saldo a añadir: '))
    listaClientes[cliente-1].add_saldo(ingreso)
    
def ver_saldo():
    banner('Nuestros clientes')
    i = 0
    for key in listaClientes:
        print(f'{i+1}) {key.nombre} {key.apellido}')
        i += 1
    cliente = int(input('¿De qué cliente desea verificar su saldo?: '))
    print(listaClientes[cliente-1].get_saldo())
    
# Clases Usuario y subclases
class Usuario:
    def __init__(self, id, nombre, apellido, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        
class Administrativo(Usuario):
    def __init__(self, id, nombre, apellido, password, fecha_incorporacion, oficina, salario, fecha_nacimiento = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.oficina = oficina
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento
        
    # Almacenar nuevos productos
    def ingresa_producto(self):
        banner('Ingresar nuevo producto')
        sku = int(input('Ingrese el SKU del nuevo producto: '))
        producto = input('Ingrese el nombre del nuevo producto: ')
        categoria = input('Ingrese la categoría del producto: ')
        valor_neto = int(input('¿Cuál es el valor del producto?: '))
        cantidad = int(input('¿Cuántas unidades tendremos de este producto?: '))
            
        nuevo_producto = Producto(sku, producto, categoria, cantidad, valor_neto)
        # Composición de la clase Producto, asignándole un proveedor
        nuevo_producto.proveedor = Proveedor("12345678-9", "La Falsa Polar", "Comercializadora de Productos de Dudoso Origen La Polar SpA", "Chile", "Jurídica")
        stock.append(nuevo_producto)
        print('El producto ha sido añadido al catálogo')
        time.sleep(2)
    
    # Ingresa nuevo cliente a la "base de datos" (necesario recodificar a modo de objetos)
    """def ingresa_cliente(self):
        banner('Ingresar nuevo cliente')
        nombre = input('Ingrese el nombre del cliente: ')
        password = input('Ingrese la contraseña del cliente: ')
        if nombre not in listaClientes:
            id = int(list(listaClientes)[-1]) + 1
            clientes[str(id)] = {'nombre' : nombre, 'password' : password}
            print('Se añadió el cliente a la base de datos')
        else:
            print('El cliente ya está registrado, se ignorarán los datos')
        time.sleep(2)"""
        
    # Mostrar clientes registrados
    def listado_clientes(self):
        banner('Nuestros clientes')
        i = 0
        for key in listaClientes:
            print(f'{i+1}) {key.nombre} {key.apellido}')
            i += 1
        
class Vendedor(Usuario):
    def __init__(self, id, nombre, apellido, password, run, fecha_incorporacion, salario, seccion = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.seccion = seccion
        self.salario = salario
        self.run = run
        self.__comision = 0
    
    # Añadir unidades a un producto del catálogo
    def actualiza_stock(self):
        banner('Actualizar stock')
        print('Seleccione el producto al cual añadiremos unidades')
        stockNames = []
        stockList = []
        i = 1
        for key in stock:
            stockNames.append(key)
            stockList.append(stock[key])
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto:'))
        cantidad = int(input('¿Cuántas unidades añadiremos?: '))
        stock[stockNames[producto-1]] = stock[stockNames[producto-1]] + cantidad
        
    # Mostrar unidades por producto
    def muestra_unidades(self):
        banner('Unidades por producto')
        for producto in stock:
            print(f'{producto}: {stock[producto]}')
            
    # Mostrar unidades de un producto en particular
    def muestra_unidades_producto(self):
        banner('Unidades de un producto')
        print('Seleccione el producto del cual quiere saber las unidades en stock')
        # Listas auxiliares para mostrar los nombres de los productos y almacenar temporalmente el stock
        stockNames = []
        stockList = []
        i = 1
        for key in stock:
            stockNames.append(key)
            stockList.append(stock[key])
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto:'))
        if producto <= len(stockList) and producto > 0:
            print(f'Tenemos actualmente {stockList[producto-1]} unidades de {stockNames[producto-1]}')
        else:
            print('Introdujo una opción incorrecta')
            time.sleep(2)


# Mostrar los productos que tienen más de X unidades
    def productos_mascantidad(self):
        banner('Productos con más que X cantidad')
        cantidad = int(input('Ingrese la cantidad: '))
        os.system('cls')
        banner(f'Productos con stock de más de {cantidad} unidades')
        for producto in stock:
            if stock[producto] > cantidad:
                print(f'{producto}: {stock[producto]}')

# Metodo para Vender Producto
    def vender_producto(self):
        banner('Venta de Producto')
        print('Seleccione el producto a vender')
        stockNames = []
        stockList = []
        i = 1
        for producto in stock:
            stockNames.append(producto.nombre)
            stockList.append(producto.stock)
            print(f'{i}) {producto.nombre}')
            i += 1
        
        productoChoose = int(input('Ingrese el número del producto:'))
        cantidad = int(input('¿Cuántas unidades venderemos?: '))
        # Comprobamos si existen suficientes unidades antes de seguir
        if cantidad > stockList[productoChoose-1]:
            print('No existen suficientes unidades para efectuar la venta')
        else:
            # Input con clientes 
            banner('Nuestros clientes')
            i = 1
            for cliente in listaClientes:
                print(f'{i}) {cliente.nombre}')
                i += 1
            # Calculamos el valor total de la compra contando comisión del vendedor y el impuesto
            impuesto = stock[productoChoose-1].get_impuesto()
            valorTotal = stock[productoChoose-1].valor_neto * impuesto * cantidad
            comision = valorTotal * 0.005
            # Comprobar que se tiene suficiente stock en la tienda
            if(stock[productoChoose-1].stock >= cantidad):
                clienteChoose = int(input('¿A que cliente le venderemos?: '))
                # Comprobar si el cliente tiene saldo suficiente
                if listaClientes[clienteChoose-1].get_saldo() >= valorTotal:
                    self.__comision += comision
                    listaClientes[clienteChoose-1].mod_saldo(-valorTotal)
                    print('La venta se ha efectuado correctamente. Muchas gracias')
                    stock[productoChoose-1].stock -= cantidad
                    # Si tenemos menos de 50 en la tienda, pedir 300 más a la bodega
                    if(stock[productoChoose-1].stock < 50):
                        if (bodega1.stock[stock[productoChoose-1].nombre] >= 300):
                            bodega1.stock[stock[productoChoose-1].nombre] -= 300
                            stock[productoChoose-1].stock += 300
                            print(f"El stock de {stock[productoChoose-1].nombre} es bajo, se están pidiendo 300 más a la bodega")
                        else:
                            print(f"El stock de {stock[productoChoose-1].nombre} es bajo, no existen suficientes unidades en la bodega para reponer")
                    time.sleep(2)
                else:
                    print('El saldo del cliente no es suficiente para efectuar la compra.')
                    time.sleep(2)
            else:
                print("No existen suficientes unidades en stock")
        

class Cliente(Usuario):
    def __init__(self, id, nombre, apellido, correo, fecha_registro, password, ciudad, volumen_compra = 0, genero = None):
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.ciudad = ciudad
        self.volumen_compra = volumen_compra
        # Atributo encapsulado
        self.__saldo = 500000
        super().__init__(id, nombre, apellido, password)
    
    #Método para añadir saldo    
    def mod_saldo(self, ingreso):
        self.__saldo += ingreso
        
    #Método para obtener saldo del cliente
    def get_saldo(self):
        return self.__saldo
    
    # Mostrar todos los productos de la tienda
    def muestra_catalogo(self):
        banner('Nuestro catálogo')
        i = 1
        for key in stock:
            print(f'{i}) {key.nombre}')
            i += 1
    
    # Solicitar compra. Se pide producto y unidades
    def solicita_compra(self):
        cliente = self.id
        banner('Efectuar compra')
        stockNames = []
        i = 1
        for key in stock:
            stockNames.append(key)
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto: '))
        cantidad = int(input('Ingrese la cantidad de unidades: '))
        # Llamamos a la función que verifica si hay stock suficiente de lo que queremos comprar
        autorizado = verifica_stock(stockNames[producto-1],cantidad)
        if autorizado:
            stock[stockNames[producto-1]] = stock[stockNames[producto-1]] - cantidad
            print('Compra autorizada y en camino')
            compras.append({'cliente' : cliente, 'producto' : stockNames[producto-1], 'cantidad' : cantidad})
        else:
            print('Compra cancelada, no hay suficiente cantidad de productos')
        print(compras)

class Producto:
    def __init__(self, sku, nombre, categoria, stock, valor_neto) -> None:
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19
        self.proveedor = None
        
    def get_impuesto(self):
        return self.__impuesto
          
class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
        
# Nueva clase Bodega
class Bodega:
    def __init__(self, id, nombre, stock = None):
        self.id = id
        self.nombre = nombre
        self.stock = stock

# Creamos los objetos con las nuevas clases
administrativo = Administrativo('a1','Paulina','Fernández','Paulina_1992','2023/03/05','Quilpué',1120000)
vendedor = Vendedor('v1','Marcos','Pérez','Marcos_45','12345678-9','2023/04/15','Informática',800000)
cliente = Cliente('1',clientes['1']['nombre'],clientes['1']['apellido'],'cliente1@pruebas.cl','2023/05/02',clientes['1']['password'],clientes['1']['ciudad'],clientes['1']['volumen_compra'])
cliente2 = Cliente('2',clientes['2']['nombre'],clientes['2']['apellido'],'cliente2@pruebas.cl','2023/05/03',clientes['2']['password'],clientes['2']['ciudad'],clientes['2']['volumen_compra'])
cliente3 = Cliente('3',clientes['3']['nombre'],clientes['3']['apellido'],'cliente3@pruebas.cl','2023/05/04',clientes['3']['password'],clientes['3']['ciudad'],clientes['3']['volumen_compra'])
cliente4 = Cliente('4',clientes['4']['nombre'],clientes['4']['apellido'],'cliente4@pruebas.cl','2023/05/05',clientes['4']['password'],clientes['4']['ciudad'],clientes['4']['volumen_compra'])
cliente5 = Cliente('5',clientes['5']['nombre'],clientes['5']['apellido'],'cliente5@pruebas.cl','2023/05/06',clientes['5']['password'],clientes['5']['ciudad'],clientes['5']['volumen_compra'])
listaClientes = [cliente,cliente2,cliente3,cliente4,cliente5]
producto1 = Producto('345675', 'Polera roja estampada', 'Vestuario Adulto', 12, 4500)
bodega1 = Bodega('bodega1', 'Bodega Santiago', {'Polera roja estampada' : 900})
stock.append(producto1)



functions = ['', '''administrativo.ingresa_cliente''', administrativo.ingresa_producto, vendedor.actualiza_stock, vendedor.muestra_unidades, vendedor.muestra_unidades_producto, cliente.muestra_catalogo, vendedor.productos_mascantidad, administrativo.listado_clientes, ingresa_saldo, ver_saldo, cliente.solicita_compra, vendedor.vender_producto]


while True:
    banner('Bienvenido')
    # Imprimir el menú
    print('1) Ingresa nuevo cliente\n2) Ingresar nuevo producto\n3) Añadir unidades a producto existente\n4) Mostrar unidades por producto\n5) Ver las unidades de un producto\n6) Muestra el catálogo\n7) Productos con más de X cantidad en stock\n8) Mostrar listado de clientes\n9) Añadir saldo al cliente\n10) Obtener saldo del cliente\n\n11) Efectuar compra\n12) Vender producto\n0) Salir')
    eleccion = int(input('Su elección: '))
    if eleccion == 0:
        print('Gracias, vuelva pronto')
        time.sleep(2)
        break
    elif eleccion >= len(functions):
        print('Ha seleccionado una opción incorrecta')
    else:
        # Llamamos a la función correspondiente a la posición en la lista
        functions[eleccion]()
    input('Pulse Enter para continuar')