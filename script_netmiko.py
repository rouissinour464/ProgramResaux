from netmiko import ConnectHandler
router = {
  'device_type': 'cisco_ios',
  'host': 'sandbox-iosxe-latest-1.cisco.com',
  'username': 'admin',
  'password': 'C1sco12345',
}
conn = ConnectHandler(**router)
temps = conn.send_command('show clock')
print(temps)

int = conn.send_command('sh ip int br')
with open("interfaces.txt", "w") as file:

    file.write(int)

print('interfaces.txt')
commands = [

   'interface loopback 8',
   'ip address 10.8.8.8 255.255.255.240',
   'no shutdown',
]

cofiguration = conn.send_config_set(commands)
print(cofiguration)

