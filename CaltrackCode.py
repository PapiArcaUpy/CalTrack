import logging
import os

# --- Logging setup ---
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s — [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Programa CalTrack iniciado")

# 1. Database and History Setup
comidas_menu = {
    "manzana": 95,
    "huevo": 78,
    "pollo": 165,
    "pizza": 285,
    "arroz": 130,
    "platano": 105,
    "ensalada": 60,
    "yogur": 100,
    "hamburguesa": 295,
    "tacos": 210
}
historial_nombres = []
historial_calorias = []
total_calorias = 0

# 2. Input Validation
while True:
    try:
        limite = int(input("Meta diaria de calorías: "))
        if limite > 0:
            logging.info(f"Meta diaria establecida: {limite} kcal")
            break
        else:
            print("Ingresa un número mayor a 0")
            logging.warning("Meta ingresada no es mayor a 0")
    except ValueError:
        print("¡Error! Ingresa un número entero.")
        logging.error("Entrada inválida para meta diaria (no es un número entero)")

# 3. Menu Loop
while True:
    opcion = input("\n[1] Menú [2] Manual [3] Salir: ")
    if opcion == "1":
        print("Disponibles:", list(comidas_menu.keys()))
        comida = input("Escribe el nombre: ").lower()
        if comida in comidas_menu:
            cal = comidas_menu[comida]
            total_calorias += cal
            historial_nombres.append(comida)
            historial_calorias.append(cal)
            logging.info(f"Comida agregada desde menú: '{comida}' ({cal} kcal)")
        else:
            print("Esa comida no está en el menú.")
            logging.warning(f"Comida no encontrada en el menú: '{comida}'")
    elif opcion == "2":
        n = input("Nombre: ")
        try:
            c = int(input("Calorías: "))
            total_calorias += c
            historial_nombres.append(n)
            historial_calorias.append(c)
            logging.info(f"Comida agregada manualmente: '{n}' ({c} kcal)")
        except ValueError:
            print("Valor inválido.")
            logging.error(f"Valor de calorías inválido al ingresar '{n}' manualmente")
    elif opcion == "3":
        logging.info("Usuario finalizó la sesión")
        break
    else:
        print("Opción no válida.")
        logging.warning(f"Opción de menú no válida ingresada: '{opcion}'")

# 4. Printing Detailed Results
print("\nRESUMEN DIARIO")
for i in range(len(historial_nombres)):
    print(f"- {historial_nombres[i]}: {historial_calorias[i]} kcal")
print(f"\nConsumo Total: {total_calorias} kcal")

restantes = limite - total_calorias
if restantes >= 0:
    print(f"Meta cumplida. Sobran {restantes} kcal")
    logging.info(f"Meta cumplida. Consumo total: {total_calorias} kcal. Sobran {restantes} kcal")
else:
    print(f"¡Alerta! Excediste el límite por {abs(restantes)} kcal")
    logging.warning(f"Límite excedido por {abs(restantes)} kcal. Consumo total: {total_calorias} kcal")
