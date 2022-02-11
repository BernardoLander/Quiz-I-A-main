


products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}


onoff = True
promo = False
clientes = {}

while onoff:

    print ("***BIENVENIDO A LA TIENDA DE ELECTRONICOS***")
    print("Indique una opcion para accesar a ella")

    user_option = input('''1. Para ver el inventario de cada categoria de productos
                        2. Para realizar una compra
                        3. Para aplicar promo a todos los productos que tengan numeros en su nombre
                        4. Para Salir de la aplicacion
                        ===>''')

    if user_option.isnumeric:

        user_option = int(user_option)

        if user_option == 1:
            #Ver inv:seleccionar categoria ==> mostrar productos por marca
            while True:
                op = input("Presione 1. Para accesar a las Laptops y 2. Para accesar a los Moviles\n==>")

                if op.isnumeric:
                    op = int(op)
                    if op == 1:

                        #Para Laptops


                        for Key,value in products["laptops"].items():

                            print (f"\nLas laptops marca {Key} en inventario son:\n")

                        for i in range(len(products["laptops"][Key])):

                            print("\n")
                            
                            for Key2, value2 in value[i].items():

                                print(f"{Key2}:,{value2}")

                    elif op == 2:
                        
                        #Para mobiles

                          for Key,value in products["mobiles"].items():

                            print (f"\nLas laptops marca {Key} en inventario son:\n")

                            for i in range(len(products["mobiles"][Key])):

                                print("\n")
                            
                                for Key2, value2 in value[i].items():

                                    print(f"{Key2}:,{value2}")

                    else:

                        print ("Porfavor ingresar numero en rango")

                else:

                    print ("Porfavor ingresar numero en el rango")
                
                op2 = input("**PRESIONE 0 PARA VER OTRO INVENTARIO Y  1 PARA SALIR AL MENU PRINCIPAL**\n===>")

                if op2.isnumeric:

                    op2 = int(op2)

                    if op2 == 1:

                        print ("Ingresando a menu principal")
                        break

                    elif op2 == 0:

                        print ("Reingresando a vizualizador de inventario")
                        break

                    else:

                        print ("Porvafor ingrese un numero valido")
                else:

                    print ("INVALID INPUT")
                


        
        elif user_option == 2:

            #Registrar cedula y nombre del cliente ==> solicitar producto pro id ==> 
            #print factura: Dni,nombre,producto y monto y/n pago y registrar

            print("Bienvenido a compras")
            nombre = input("Ingrese su nombre porfavor\n==>")
            dni = input ("Ingrese su cedula por favor\n==>")
            op = input ("Por favor ingrese 1. para comprar mobiles o 2. para comprar Laptops\n==>")
            id_tobuy = input ("Por favor ingrese el id del producto a comprar\n==>")

            if op.isnumeric and id_tobuy:

                op = int(op)

                if op == 1:

                    for Key,value in products["mobiles"].items():

                        for i in range(len(products["mobiles"][Key])):

                            print("\n")

                            for Key2, value2 in value[i].items():

                                    if id_tobuy in value[i].items():

                                        (f"{Key2}:,{value2}")



        elif user_option == 3:

            promo = True
            #Aplicar promo a productos que tengan numero en su numbre
        
        elif user_option == 4:

            print ("Hasta Luego...")
            onoff = False



