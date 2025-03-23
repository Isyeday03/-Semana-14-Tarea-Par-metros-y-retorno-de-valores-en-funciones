# Programa de cálculo de descuentos para Microcomercial PROLCOM

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.
    
    Args:
        monto_total (float): El monto total de la compra
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar. Por defecto es 10%.
        
    Returns:
        float: El monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Catálogo de productos alimenticios de Microcomercial PROLCOM
productos = {
    "Arroz (kg)": 25,
    "Frijoles (kg)": 30,
    "Aceite de cocina (1L)": 45,
    "Pasta (500g)": 15,
    "Atún en lata (pack 3)": 60,
    "Café (250g)": 75,
    "Leche (1L)": 20,
    "Pan de caja": 35,
    "Huevos (docena)": 40,
    "Azúcar (kg)": 28
}

# Mostrar catálogo de productos
print("BIENVENIDO A MICROCOMERCIAL PROLCOM")
print("===================================")
print("\nCATÁLOGO DE PRODUCTOS ALIMENTICIOS:")
print("----------------------------------")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")

# Simulación de compra 1: Usando el descuento predeterminado (10%)
compra1 = 25 + 30 + 45 + 40  # Arroz + Frijoles + Aceite + Huevos
print("\nCOMPRA 1:")
print(f"Productos: Arroz (kg), Frijoles (kg), Aceite de cocina (1L), Huevos (docena)")
print(f"Monto total de compra: ${compra1}")
descuento1 = calcular_descuento(compra1)  # Utilizando el descuento predeterminado del 10%
monto_final1 = compra1 - descuento1
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")

# Simulación de compra 2: Especificando un porcentaje de descuento diferente (15%)
compra2 = 75 + 20 + 35 + 28 + 15  # Café + Leche + Pan + Azúcar + Pasta
print("\nCOMPRA 2:")
print(f"Productos: Café (250g), Leche (1L), Pan de caja, Azúcar (kg), Pasta (500g)")
print(f"Monto total de compra: ${compra2}")
descuento2 = calcular_descuento(compra2, 15)  # Utilizando un descuento del 15%
monto_final2 = compra2 - descuento2
print(f"Descuento aplicado (15%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")

print("\nGracias por su compra en Microcomercial PROLCOM!")