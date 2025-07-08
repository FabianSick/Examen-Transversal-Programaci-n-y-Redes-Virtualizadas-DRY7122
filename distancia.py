import openrouteservice
from openrouteservice import convert
import sys

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjBkYTUzNTY3ZjMyZDQzNmM5YTgyYzI5OGZlMWI0NjEzIiwiaCI6Im11cm11cjY0In0="

cliente = openrouteservice.Client(key=API_KEY)

# Coordenadas aproximadas de algunas ciudades de Chile y Perú
ciudades = {
    "santiago": (-70.6483, -33.4569),
    "valparaiso": (-71.6127, -33.0472),
    "arica": (-70.3126, -18.4783),
    "lima": (-77.0428, -12.0464),
    "arequipa": (-71.5370, -16.4090),
    "cusco": (-71.9675, -13.5320)
}

transportes = {
    "1": "driving-car",
    "2": "cycling-regular",
    "3": "foot-walking"
}

print("Bienvenido al calculador de distancia entre ciudades de Chile y Perú.")

while True:
    print("\nEscriba 's' para salir.")
    origen = input("Ciudad de origen: ").strip().lower()
    if origen == "s":
        break
    destino = input("Ciudad de destino: ").strip().lower()
    if destino == "s":
        break

    if origen not in ciudades or destino not in ciudades:
        print("❌ Una o ambas ciudades no están registradas.")
        print("Ciudades disponibles:", ", ".join(ciudades.keys()))
        continue

    print("\nSeleccione medio de transporte:")
    print("1 - Auto")
    print("2 - Bicicleta")
    print("3 - A pie")
    tipo = input("Opción (1/2/3): ")

    if tipo not in transportes:
        print("❌ Medio de transporte no válido.")
        continue

    coords = (ciudades[origen], ciudades[destino])

    try:
        ruta = cliente.directions(coords, profile=transportes[tipo], format='geojson')
        distancia_m = ruta['features'][0]['properties']['segments'][0]['distance']
        duracion_s = ruta['features'][0]['properties']['segments'][0]['duration']
        narrativa = ruta['features'][0]['properties']['segments'][0]['steps']

        print(f"\n📍 Distancia entre {origen.title()} y {destino.title()}:")
        print(f"  ➤ {distancia_m / 1000:.2f} kilómetros")
        print(f"  ➤ {distancia_m * 0.000621371:.2f} millas")
        print(f"⏱️ Duración estimada: {duracion_s / 60:.1f} minutos\n")

        print("🧭 Narrativa del viaje:")
        for paso in narrativa:
            print(f"• {paso['instruction']}")

    except Exception as e:
        print("❌ Error al calcular la ruta:", e)
