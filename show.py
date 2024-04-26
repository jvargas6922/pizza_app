def mostrar_ingredientes(ingredientes):
    print(f'Su masa es: {ingredientes["masa"]}')
    print(f'Su salsa es: {ingredientes["salsa"]}')
    print('Los ingredientes de su Pizza:')
    for ing in ingredientes['ingredientes']:
        print(f'- {ing}')

if __name__ == '__main__':
    ingredientes_prueba = {
        'masa':'Masa Tradicional',
        'salsa':'Salsa de Tomate',
        'ingredientes':['Queso','Tomate','Champiñones','Jamón']
    }
    mostrar_ingredientes(ingredientes_prueba)