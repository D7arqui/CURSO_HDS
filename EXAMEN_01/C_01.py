carrito = {}
total_costo = 0
while True:
    articulo = input("Ingresa el artículo (o escribe 'terminar' para finalizar): ")
    if articulo.lower() == 'terminar':
        break
    precio = float(input("Ingresa el precio del artículo: "))
    carrito[articulo] = precio
    total_costo += precio
print("\nLista de la compra:")
for articulo, precio in carrito.items():
    print(f"{articulo}: s/.{precio:.2f}")
print(f"\nCosto total: s/.{total_costo:.2f}")