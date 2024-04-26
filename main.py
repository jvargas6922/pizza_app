from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo

ingredientes_orden ={
    'masa':'Masa Tradicional',
    'salsa':'Salsa de Tomate',
    'ingredientes':['Queso']
}

"""
opcion = input('''¿Qué desea realizar?
 1. Cambiar tipo de Masa
 2. Cambiar tipo de Salsa
 3. Agregar Ingredientes
 4. Eliminar Ingredientes
 5. Ordenar con los Ingredientes Actuales
 0. Consultar ingredientes de la pizza
 Otro Número cancelará el pedido.
 > ''')
 """

print('Bienvenido a la Pizzería Python')
print('Gracias por ordenar con nosotros')
while True:
    opcion = opcion = input('''¿Qué desea realizar?
    1. Cambiar tipo de Masa
    2. Cambiar tipo de Salsa
    3. Agregar Ingredientes
    4. Eliminar Ingredientes
    5. Ordenar con los Ingredientes Actuales
    0. Consultar ingredientes de la pizza
    Otro Número cancelará el pedido.
    > ''')

    if opcion == '1':
        eleccion = input('''¿Escoja el tipo de masa?
        T. Masa Tradicional
        D. Masa Delgada
        B. Masa con Bordes de Queso
        > ''').upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)

    elif opcion == '2':
        eleccion = input('''¿Seleccione su tipo e salsa?
        T. Salsa de tomate
        A. Salsa Alfredo
        B. Salsa Barbecue
        P. Salsa Pesto
        > ''').upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)

    elif opcion == '3':
        eleccion = int(input('''¿Qué ingrediente desea agregar?
        1. Tomate
        2. Champiñones
        3. Aceituna
        4. Cebolla
        5. Pollo
        6. Jamón
        7. Carne
        8. Tocino
        9. Queso
        > '''))
        ingredientes_orden = agregar_ingredientes(ingredientes_orden, eleccion)

    elif opcion == '4':
        eleccion = int(input('''¿Qué ingrediente desea quitar?
        1. Tomate
        2. Champiñones
        3. Aceituna
        4. Cebolla
        5. Pollo
        6. Jamón
        7. Carne
        8. Tocino
        9. Queso
        > '''))
        ingredientes_orden = quitar_ingredientes(ingredientes_orden, eleccion)

    elif opcion == '5':
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'La pizza estará lista en {tiempo} minutos')
        ordenar = input('¿Desea ordenar la pizza? (S/N)').upper()

        if ordenar == 'S':
            print('Gracias por ordenar con nosotros')
            print('Difrute su pizza')
            exit()

    elif opcion == '0':
        mostrar_ingredientes(ingredientes_orden)

    else:
        print('Su pedido ha sido cancelado. Gracias por contactarnos. a la Pizzería Python')
        exit()