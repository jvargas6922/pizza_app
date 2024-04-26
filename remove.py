def quitar_ingrediente(ingredientes, eleccion):
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo','Jamón','Carne','Tocino','Queso']
    quitar = disponibles[eleccion-1]

    if quitar in ingredientes['ingredientes']:
        ingredientes['ingredientes'].remove(quitar)
        print(f'Se ha quitado {quitar}')
    elif len(ingredientes['ingredientes']) == 0:
        print('No hay ningún ingrediente que quitar')
    else:
        print('No se puede quitar ese ingrediente, porque no está incluido')

    return ingredientes

if __name__ == '__main__':
    ingredientes_prueba = {
        'masa':'Masa Tradicional',
        'salsa':'Salsa de Tomate',
        'ingredientes':['Queso']
    }
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

    ingredientes = quitar_ingrediente(ingredientes_prueba, eleccion)
    print(ingredientes)