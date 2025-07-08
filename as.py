as_num = int(input("Ingrese el número de AS (Autonomous System): "))

if 64512 <= as_num <= 65534:
    print(f"El AS {as_num} es un AS PRIVADO.")
else:
    print(f"El AS {as_num} es un AS PÚBLICO.")
