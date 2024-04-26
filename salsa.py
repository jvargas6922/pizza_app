def tipo_salsa(ingredientes, eleccion):
    if eleccion == 'T':
        ingredientes['salsa'] = 'Salsa de Tomate'
    elif eleccion == 'A':
        ingredientes['salsa'] = 'Salsa Alfredo'
    elif eleccion == 'B':
        ingredientes['salsa'] = 'Salsa Barbecue'
    elif eleccion == 'P':
        ingredientes['salsa'] = 'Salsa Pesto'

    if eleccion in ['T','A','B','P']:
        print(f'Su salsa se cambió a {ingredientes["salsa"]}')
    else:
        print('No se ha cambiado su tipo de Salsa')
    return ingredientes

if __name__ == '__main__':
    ingredientes_prueba = {
        'masa':'Masa Tradicional',
        'salsa':'Salsa de Tomate',
        'ingredientes':['Queso']
    }
    eleccion = input('''¿Seleccione su tipo e salsa?
        T. Salsa de tomate
        A. Salsa Alfredo
        B. Salsa Barbecue
        P. Salsa Pesto
        > ''').upper()
    ingredientes = tipo_salsa(ingredientes_prueba, eleccion)
    print(ingredientes)