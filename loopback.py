from ncclient import manager

router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}

config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>111.111.111.111</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    respuesta = m.edit_config(target="running", config=config_loopback)
    print(respuesta)
