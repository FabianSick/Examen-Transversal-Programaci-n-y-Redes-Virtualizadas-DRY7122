from ncclient import manager

# Datos de conexión
router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}

# Nuevo nombre para el router
nuevo_nombre = "COFRE-OPAZO"

config_hostname = f"""
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>{nuevo_nombre}</hostname>
  </native>
</config>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    respuesta = m.edit_config(target="running", config=config_hostname)
    print(respuesta)
