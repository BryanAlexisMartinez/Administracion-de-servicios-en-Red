from netmiko import ConnectHandler

devices = '''
R1
R2
R3
R4
R5
R6
R7
R8
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'admin'
password = '1234'
verbose = True

for device in devices:
        print(" Conectando al Dispositivo: " + device)
        net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()

        output = net_connect.send_command('show run | sec ospf')
        ospf_commands = ['router ospf 1', 'net 0.0.0.0 255.255.255.255 area 0']
        if not 'router ospf' in output:
            print('OSPF no esta activo en este dispositivo: ' + device)
            answer = input('Quiere habilitar la configuracion OSPF en: ' + device + ' <y/n> ')
            if answer == 'y':
                output = net_connect.send_config_set(ospf_commands)
                print(output)
                print('OSPF configurado correctamente')
            else:
                print('No se ha configurado OSPF correctamente')

        else:
            print("Ya esta configurado OSPF en este dispositivo: " + device)