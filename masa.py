def tipo_masa(ingredientes, eleccion):
    if eleccion == 'T':
        ingredientes['masa'] = 'Masa Tradicional'
    elif eleccion == 'D':
        ingredientes['masa'] = 'Masa Delgada'
    elif eleccion == 'B':
        ingredientes['masa'] = 'Masa con Bordes de Queso'

    if eleccion in ['T','D','B']:
        print(f'Su masa se cambió a {ingredientes["masa"]}')
    else:
        print('No se ha cambiado su tipo de Masa')

    return ingredientes

if __name__ == '__main__':
    ingredientes_prueba = {
        'masa':'Masa Tradicional',
        'salsa':'Salsa de Tomate',
        'ingredientes':['Queso']
    }
    eleccion = input('''¿Qué desea realizar?
        1. Cambiar tipo de Masa
        2. Cambiar tipo de Salsa
        3. Agregar Ingredientes
        4. Eliminar Ingredientes
        5. Ordenar con los Ingredientes Actuales
        0. Consultar ingredientes de la pizza
        Otro Número cancelará el pedido.
        > ''').upper()
    ingredientes = tipo_masa(ingredientes_prueba, eleccion)
    print(ingredientes)